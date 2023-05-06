import os
import json
import argparse

# Example of how to call the script, please use:
# python create_section_args.py -t 1 -l "My Section" -i my_section -g 0 -c "your_content_file.json"
# Example details and description
#-t 1: This specifies the section type, with 1 meaning a "section". It corresponds to the --type argument in the script.
#-l "My Section": This sets the label (name) of the section or group. It corresponds to the --label argument in the script.
#-i my_section: This sets the unique identifier for the section or group. It corresponds to the --id argument in the script.
#-g 0: This specifies the parent group ID. If set to 0, the section is added to the main branch. It corresponds to the --group argument in the script.
#-c "your_content_file.json": This provides the path to the JSON file containing content objects for the section. It corresponds to the --content argument in the script.
# JSON file content format should be as follows:
# [
# {"type":"t","v":[1,"Header h1 Example"]},
# {"type":"p","v":"Paragraph Example."},
# {"type":"s","v":"{\n    'Code': 'Block',\n    'v': [\n        5,\n        \"Your &lt;b&gt;SNIPPET&lt;br&gt; Example&lt;/b&gt;\"\n    ]\n}"},
# {"type":"ta","v":{"h":["Header 1", "Header 2"],"r":[["Row 1 Col 1", "Row 1 Col 2"],["Row 2 Col 1", "Row 2 Col 2"]]}}
# ]
# Please ensure you use ONLY the supported objects as shown in the examples above. Other HTML tags like 'li', etc., are NOT supported.

def generate_html(input_arr):
    output_str = '<div class="container mt-5 row offset-1 col-10">\n'
    for obj in input_arr:
        if 'type' not in obj or 'v' not in obj:
            return {"success": False, "error": "Input format is invalid."}
        if obj['type'] == 't':
            if not isinstance(obj['v'], list) or len(obj['v']) != 2 or not isinstance(obj['v'][0], int) or not isinstance(obj['v'][1], str):
                return {"success": False, "error": "Invalid input format for title object."}
            output_str += f'<h{obj["v"][0]} class="mb-4 text-center">{obj["v"][1]}</h{obj["v"][0]}>\n'
        elif obj['type'] == 'ta':
            if not isinstance(obj['v'], dict) or 'h' not in obj['v'] or 'r' not in obj['v'] or not isinstance(obj['v']['h'], list) or not isinstance(obj['v']['r'], list):
                return {"success": False, "error": "Invalid input format for table object."}
            for header in obj['v']['h']:
                if not isinstance(header, str):
                    return {"success": False, "error": "Invalid input format for table header."}
            for row in obj['v']['r']:
                if not isinstance(row, list):
                    return {"success": False, "error": "Invalid input format for table row."}
                for col in row:
                    if not isinstance(col, str):
                        return {"success": False, "error": "Invalid input format for table cell."}
            output_str += '<table class="table">\n<thead>\n<tr>\n'
            for header in obj['v']['h']:
                output_str += f'<th class="text-center align-middle">{header}</th>\n'
            output_str += '</tr>\n</thead>\n<tbody>\n'
            for row in obj['v']['r']:
                output_str += '<tr>\n'
                for col in row:
                    output_str += f'<td class="text-center align-middle">{col}</td>\n'
                output_str += '</tr>\n'
            output_str += '</tbody>\n</table>\n'
        elif obj['type'] == 's':
            if not isinstance(obj['v'], str):
                return {"success": False, "error": "Invalid input format for code object."}
            output_str += f'<pre><code>{obj["v"]}</code></pre>\n'
        elif obj['type'] == 'p':
            if not isinstance(obj['v'], str):
                return {"success": False, "error": "Invalid input format for paragraph object."}
            output_str += f'<p>{obj["v"]}</p>\n'
        else:
            return {"success": False, "error": f"Invalid object type '{obj['type']}'."}
    output_str += '</div>'
    return {"success": True, "html": output_str}

# Read the sections JSON file
with open('sections.json', 'r') as file:
    sections = json.load(file)

# Set up argument parser
parser = argparse.ArgumentParser(description='Create a section in the sections.json file')
parser.add_argument('-t', '--type', type=int, required=True, help='Section type (1="section", 2="group")')
parser.add_argument('-l', '--label', type=str, required=True, help='Section/Group label')
parser.add_argument('-i', '--id', type=str, required=True, help='Section/Group ID (unique)')
parser.add_argument('-g', '--group', type=str, required=True, help='Parent Group ID (0 for none)')
parser.add_argument('-c', '--content', type=str, help='Path to the JSON file containing content objects')

# Parse arguments
args = parser.parse_args()

# Assign the parsed arguments to variables
section_type = args.type
section_label = args.label
section_id = args.id
section_group_id = args.group

def find_group(groups, group_id):
    for group in groups:
        if group['type'] == 'group' and group['group_id'] == group_id:
            return group
        elif group['type'] == 'group':
            found_group = find_group(group['group'], group_id)
            if found_group:
                return found_group
    return None

def is_unique_id(sections, section_id):
    for section in sections:
        if section['type'] == 'section' and section['section_id'] == section_id:
            return False
        elif section['type'] == 'group':
            if not is_unique_id(section['group'], section_id):
                return False
    return True

if not is_unique_id(sections, section_id):
    print("The provided ID is not unique.")
else:
    if section_type == 1 and args.content:
        with open(args.content, 'r') as content_file:
            section_content = json.load(content_file)

        html_output = generate_html(section_content)
        if not html_output["success"]:
            print("Error: " + html_output["error"])
        else:
            output_path = f"sections/{section_group_id}/{section_id}.html" if section_group_id != "0" else f"sections/{section_id}.html"
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            with open(output_path, 'w') as file:
                file.write(html_output["html"])

            section_obj = {
                "type": "section",
                "section_id": section_id,
                "label": section_label,
                "url": output_path
            }

            if section_group_id != "0":
                target_group = find_group(sections, section_group_id)
                if target_group:
                    target_group["group"].append(section_obj)
                else:
                    print("The specified group ID does not exist.")
            else:
                sections.append(section_obj)
    elif section_type == 2:
        sections.append({
            "type": "group",
            "label": section_label,
            "group_id": section_id,
            "group": []
        })
    else:
        print("Invalid section type.")

    with open('sections.json', 'w') as file:
        json.dump(sections, file, indent=2)