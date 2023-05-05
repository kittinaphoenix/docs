# Example with all valid objects
input_arr = [
    {"type": "t", "v": [1, "Project Documentation"]},
    {"type": "p", "v": "This project is a website with a left-hand side menu that allows users to navigate through different sections."},
    {"type": "p", "v": "The main.js file contains JavaScript functions that handle the loading and display of the pages. The populateMenu() function generates the menu HTML based on the \"sections\" JSON data, while the loadContent() function fetches the content of the page and displays it on the right-hand side of the site (For run locally needs to disable CORS)."},
    {"type": "t", "v": [2, "Structure"]},
    {"type": "p", "v": "The repository is structured as follows:"},
    {"type": "p", "v": "css/: contains CSS files used by the project."},
    {"type": "p", "v": "libs/: contains external libraries used by the project."},
    {"type": "p", "v": "pyGenerator/generator.py: contains Python code for generating HTML documentation."},
    {"type": "p", "v": "sections/: contains HTML files for different sections of the project."},
    {"type": "p", "v": "src/main.js: contains JavaScript code for the main page."},
    {"type": "p", "v": "src/sections.js: contains JavaScript code for the sections."},
    {"type": "p", "v": "webfonts/: contains web fonts used by the project."},
    {"type": "p", "v": "index.html: the main HTML file for the project."},
    {"type": "t", "v": [2, "Installation"]},
    {"type": "s", "v": 
        "Clone this repository. & Open index.html in your browser to view the documentation site."
    },
    {"type": "t", "v": [2, "Usage"]},
    {"type": "p", "v": "The sections.js file is a JavaScript module that exports an array of objects, where each object represents a section of the website. The array is called sections and it contains different types of sections such as direct sections and tree sections."},
    {"type": "p", "v": "A direct section is a simple section that has a label and a URL key-value pair. When the user clicks on the label, the website loads the content from the URL specified."},
    {"type": "p", "v": "A tree section is a section that has a label and a tree key-value pair. The tree is an array of objects that can be either direct sections or tree sections. This creates a hierarchical structure where the parent section contains child sections that can also contain child sections."},
    {"type": "p", "v": "The url key-value pair is important because it specifies the location of the content that needs to be loaded when the user clicks on a section. This location can be an HTML file, a JSON file, or any other file format that contains the content to be displayed."},
    {"type": "p", "v": "The sections.js module is used by the main.js file to generate the menu on the left-hand side of the website. When the user clicks on a section in the menu, the loadContent function in main.js is called with the URL of the section. The loadContent function fetches the content from the specified URL and inserts it into the container element on the right-hand side of the website."},
    {"type": "t", "v": [2, "Known Issues"]}
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