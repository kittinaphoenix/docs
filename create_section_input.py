import os
import json

# Example with all valid objects
example = [
{"type":"t","v":[1,"Header h1 Example"]},
{"type":"p","v":"Parragraph Example."},
{"type":"s","v":"{\n    'Code': 'Block',\n    'v': [\n        5,\n        \"Your &lt;b&gt;SNIPPET&lt;br&gt; Example&lt;/b&gt;\"\n    ]\n}"},
{"type":"ta","v":{"h":["Header 1", "Header 2"],"r":[["Row 1 Col 1", "Row 1 Col 2"],["Row 2 Col 1", "Row 2 Col 2"]]}}
]

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

# Accept the section parameters
section_type = int(input('Section type (1="section", 2="group"): '))
section_label = input('Section/Group label: ')
section_id = input('Section/Group ID (unique): ')
section_group_id = input('Parent Group ID (0 for none): ')

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
    if section_type == 1:
        section_content = input('Section content (based on provided example): ')
        section_content = json.loads(section_content)

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