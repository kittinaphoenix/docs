# Docs

This project is a website with a left-hand side menu that allows users to navigate through different sections. The left-hand menu is generated dynamically based on [src/sections.js](./src/sections.js), which defines the structure of the menu and the URLs of the pages that the user can navigate to.

The main.js file contains JavaScript functions that handle the loading and display of the pages. The populateMenu() function generates the menu HTML based on the "sections" JSON data, while the loadContent() function fetches the content of the page and displays it on the right-hand side of the site (For run locally needs to disable CORS).

## Structure

The repository is structured as follows:

- [css/](./css/): contains CSS files used by the project.
- [libs/](./libs/): contains external libraries used by the project.
- [sections/](./sections/): contains HTML files for different sections of the project.
- [src/main.js](./src/main.js): contains JavaScript code for the main page.
- [webfonts/](./webfonts/): contains web fonts used by the project.
- [create_section_input.py](./create_section_input.py): contains Python code for generating sections for this project (with input).
- [create_section_args.py](./create_section_args.py): contains Python code for generating sections for this project (with args) (read documentation inside the file).
- [create_section.sh](./create_section.sh): calls the [create_section_args.py](./create_section_args.py) (read documentation inside the file).
- [sections.json](./sections.json): contains the array for sections.
- [sections.template.json](./sections.template.json): template example for the sections.json file format.
- [index.html](./index.html): the main HTML file for the project.


## Installation

1. Clone this repository.
2. Open `index.html` in your browser to view the documentation site.

## Usage

The sections.json file contains an array of objects, where each object represents a section of the website. The array contains two different types of sections:'section' & 'group'.

A 'section' type is a simple section that has a label and a URL key-value pair. When the user clicks on the label, the website loads the content from the URL specified.

A 'group' section is a section that has a label and a tree key-value pair. The tree is an array of objects that can be either sections or nested groups. This creates a hierarchical structure where the parent group section contains child group sections that can also contain more sub groups or mixed section/groups.

The url key-value pair is important because it specifies the location of the content that needs to be loaded when the user clicks on a section (only present on 'section' type). This location is an HTML file that contains the content to be displayed.

The main.js fetches the sections.json file to generate the menu on the left-hand side of the website. When the user clicks on a section in the menu, the loadContent function in main.js is called with the URL of the section. The loadContent function fetches the content from the specified URL and inserts it into the container element on the right-hand side of the website.

## Known Issues:

The application currently does not verify the integrity of sections.json, which could potentially lead to errors if the file is not properly formatted.
While the nested group structure of the sections array is flexible and allows for easy customization, it does not verify the integrity of the structure and its respective direct URLs. If the structure or URLs are incorrect, this could result in errors.
The application also does not validate the integrity of each HTML file loaded, which could potentially result in errors if the file is not properly formatted or if there are issues with the code.
Currently, the application does not run scripts inside the sections, which may limit functionality for certain use cases.

## Generator [create_section_input.py](./create_section_input.py) & [create_section_args.py](./create_section_args.py)
Experimental Python script that generates a sections and adds it to the sections.json array, and generates an HTML file inside the sections folder. This script is not required for the project to function and is intended for advanced users who wish to generate HTML programmatically. More specific usage is detailed on the respective section documentation.

## Contributing

Please submit any issues or pull requests on the GitHub repository.
