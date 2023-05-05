# Example snippet code
input_arr = [
    {"type": "t", "v": [1, "Documentation Example"]},
    {"type": "p", "v": "This is an example of how to use the <code>generate_html()</code> method in the <code>pyGenerator/generator.py</code> module to generate an HTML document template based on a dummy template."},
    {"type": "p", "v": "Modify the <code>input_arr</code> providing a valid array based on the format below."},
    {"type": "t", "v": [2, "Possible objects for the array may include:"]},
    {"type": "ta", "v": {
        "h": ["Name", "Type <span style=\"color:grey;font-weight: 400;\">(Type)</span>", "v <span style=\"color:grey;font-weight: 400;\">(Value)</span>", "Description"],
        "r": [
            ["title", "t", "Array <code>[HeaderSize(Number),Text(String)]</code>", "Generates a title with the header size specified and with the text specified."],
            ["Parragraph", "p", "Text(String)", "Generates a parragraph with the text specified."],
            ["table", "ta", "Array <code>[h(Array),r(Array[Array])]</code>", "Generates a table with headers, and rows."],
            ["Snippet", "s", "Text(String)", "Generates a block code snippet."]
        ]
    }},
    {"type": "t", "v": [5, "Object Title example:"]},
    {"type": "s", "v": "{\n    'type': 't',\n    'v': [\n        5,\n        \"Your &lt;b&gt;title&lt;br&gt; here&lt;/b&gt;\"\n    ]\n}"},
    {"type": "t", "v": [5, "Object Title Key Value list:"]},
    {"type": "ta", "v": {
        "h": ["Name", "Type", "Description"],
        "r": [
            ["<code>[0]</code> Header Size", "Number", "From <code>1</code> to <code>5</code>. Is the header size."],
            ["<code>[1]</code> Header Text", "String", "The text inside the element, can content valid HTML tags, such as <code>&lt;b&gt;Mi&lt;br&gt;Title&lt;/b&gt;</code>"]
        ]
    }},
    {"type": "t", "v": [5, "Object Parragraph example:"]},
    {"type": "s", "v": "{\n    'type': 'p',\n    'v': \"Your &lt;b&gt;parragraph&lt;br&gt;text&lt;/b&gt;here.\"\n}"},
    {"type": "p", "v": "In this case the key <code>'v'</code> is directly the string of the parragraph, which can also include valid HTML Tags as the title."},
     {"type": "t", "v": [5, "Object Table example:"]},
    {"type": "s", "v": "{\n    'type': 'ta',\n    'v': {\n        'h': ['Header1', 'Header2'],\n        'r': [\n            ['Row1 Col1', 'Row1 Col2'],\n            ['Row2 Col1', 'Row2 Col2']\n        ]\n    }\n}"},
    {"type": "t", "v": [5, "Object Table Key Value list:"]},
    {"type": "ta", "v": {
        "h": ["Name", "Type", "Description"],
        "r": [
            ["<code>h</code> Headers", "Array", "An array of strings, each representing a header for the table."],
            ["<code>r</code> Rows", "Array[Array]", "An array of arrays, where each inner array represents a table row with its respective cell values."]
        ]
    }},
    {"type": "t", "v": [5, "Object Snippet example:"]},
    {"type": "s", "v": "{\n    'type': 's',\n    'v': \"def hello_world():\\n    print('Hello, World!')\"\n}"}
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
                output_str += f'<th class="text-center">{header}</th>\n'
            output_str += '</tr>\n</thead>\n<tbody>\n'
            for row in obj['v']['r']:
                output_str += '<tr>\n'
                for col in row:
                    output_str += f'<td class="text-center">{col}</td>\n'
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

# Generate the HTML
result = generate_html(input_arr)

if result["success"]:
    # Output the generated HTML
    print(result["html"])
else:
    # Output the error message
    print(result["error"])