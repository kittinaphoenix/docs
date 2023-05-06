#!/bin/sh

# Example details and description
#-t 1: This specifies the section type, with 1 meaning a "section". It corresponds to the --type argument in the script.
#-l "My Section": This sets the label (name) of the section or group. It corresponds to the --label argument in the script.
#-i my_section: This sets the unique identifier for the section or group. It corresponds to the --id argument in the script.
#-g 0: This specifies the parent group ID. If set to 0, the section is added to the main branch. It corresponds to the --group argument in the script.
#-c "create_section_args_template.json": This provides the path to the JSON file containing content objects for the section. It corresponds to the --content argument in the script.
# JSON file content format should be as follows:
# [
# {"type":"t","v":[1,"Header h1 Example"]},
# {"type":"p","v":"Paragraph Example."},
# {"type":"s","v":"{\n    'Code': 'Block',\n    'v': [\n        5,\n        \"Your &lt;b&gt;SNIPPET&lt;br&gt; Example&lt;/b&gt;\"\n    ]\n}"},
# {"type":"ta","v":{"h":["Header 1", "Header 2"],"r":[["Row 1 Col 1", "Row 1 Col 2"],["Row 2 Col 1", "Row 2 Col 2"]]}}
# ]
# Please ensure you use ONLY the supported objects as shown in the examples above. Other HTML tags like 'li', etc., are NOT supported.

while [ "$#" -gt 0 ]; do
  case "$1" in
    -t|--type)
      section_type="$2"
      shift 2
      ;;
    -l|--label)
      section_label="$2"
      shift 2
      ;;
    -i|--id)
      section_id="$2"
      shift 2
      ;;
    -g|--group)
      section_group_id="$2"
      shift 2
      ;;
    -c|--content)
      section_content="$2"
      shift 2
      ;;
    *)
      echo "Unknown option: $1"
      exit 1
      ;;
  esac
done

if [ -z "$section_type" ] || [ -z "$section_label" ] || [ -z "$section_id" ] || [ -z "$section_group_id" ]; then
  echo "Error:"
  echo "Missing required arguments (-t,-l,-i,-g must be present)"
  exit 1
fi

if [ "$section_type" = "1" ] && [ -z "$section_content" ]; then
  echo "Error:"
  echo "Missing required argument -c is required when type is 'section'"
  exit 1
fi

output=$(python3 create_section_args.py -t "$section_type" -l "$section_label" -i "$section_id" -g "$section_group_id" -c "$section_content")

if [ $? -ne 0 ]; then
  echo "Error:"
  echo "$output"
else
  echo "Success"
fi
