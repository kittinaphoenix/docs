# Docs

This project is a website with a left-hand side menu that allows users to navigate through different sections. The left-hand menu is generated dynamically based on [src/sections.js](./src/sections.js), which defines the structure of the menu and the URLs of the pages that the user can navigate to.

The main.js file contains JavaScript functions that handle the loading and display of the pages. The populateMenu() function generates the menu HTML based on the "sections" JSON data, while the loadContent() function fetches the content of the page and displays it on the right-hand side of the site (For run locally needs to disable CORS).

## Structure

The repository is structured as follows:

- [css/](./css/): contains CSS files used by the project.
- [libs/](./libs/): contains external libraries used by the project.
- [pyGenerator/generator.py](./pyGenerator/generator.py): contains Python code for generating HTML documentation.
- [sections/](./sections/): contains HTML files for different sections of the project.
- [src/main.js](./src/main.js): contains JavaScript code for the main page.
- [src/sections.js](./src/sections.js): contains JavaScript code for the sections.
- [webfonts/](./webfonts/): contains web fonts used by the project.
- [index.html](./index.html): the main HTML file for the project.


## Installation

1. Clone this repository.
2. Open `index.html` in your browser to view the documentation site.

## Usage

The sections.js file is a JavaScript module that exports an array of objects, where each object represents a section of the website. The array is called sections and it contains different types of sections such as direct sections and tree sections.

A direct section is a simple section that has a label and a URL key-value pair. When the user clicks on the label, the website loads the content from the URL specified.

A tree section is a section that has a label and a tree key-value pair. The tree is an array of objects that can be either direct sections or tree sections. This creates a hierarchical structure where the parent section contains child sections that can also contain child sections.

The url key-value pair is important because it specifies the location of the content that needs to be loaded when the user clicks on a section. This location can be an HTML file, a JSON file, or any other file format that contains the content to be displayed.

The sections.js module is used by the main.js file to generate the menu on the left-hand side of the website. When the user clicks on a section in the menu, the loadContent function in main.js is called with the URL of the section. The loadContent function fetches the content from the specified URL and inserts it into the container element on the right-hand side of the website.

## Known Issues:

The application currently does not verify the integrity of sections.js, which could potentially lead to errors if the file is not properly formatted.
While the nested tree structure of the sections array is flexible and allows for easy customization, it does not verify the integrity of the tree structure and its respective direct URLs. If the structure or URLs are incorrect, this could result in errors when loading pages.
The application also does not validate the integrity of each HTML file loaded, which could potentially result in errors if the file is not properly formatted or if there are issues with the code.
Currently, the application does not run scripts inside the sections, which may limit functionality for certain use cases.

## Generator [pyGenerator/generator.py](./pyGenerator/generator.py)
The pyGenerator folder contains an experimental Python script that generates HTML based on an input array. This script is not required for the project to function and is intended for advanced users who wish to generate HTML programmatically. To use the script, modify the input_arr array in generator.py and run the script from the command line: python generator.py. The generated HTML will be printed to the console.

## Contributing

Please submit any issues or pull requests on the GitHub repository.
