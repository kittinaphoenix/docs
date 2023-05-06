#!/bin/sh

#-t is the type:'1' for section, '2' for group
#-i is the id (must be unique)
#-g is the parent group id, if '0' then the section is added to the main branch
#-c is the content (see documentation for supported format)

# Content Array objects (array must be in a single line):
# - "t": Header (h1 to h5), e.g. {"type":"t","v":[1,"Header h1 Example"]}
# - "p": Paragraph, e.g. {"type":"p","v":"Paragraph Example."}
# - "s": Snippet, e.g. {"type":"s","v":"{\n    '\''Code'\'': '\''Block'\'',\n    '\''v'\'': [\n        5,\n        \"Your &lt;b&gt;SNIPPET&lt;br&gt; Example&lt;/b&gt;\"\n    ]\n}"}
# - "ta": Table, e.g. {"type":"ta","v":{"h":["Header 1", "Header 2"],"r":[["Row 1 Col 1", "Row 1 Col 2"],["Row 2 Col 1", "Row 2 Col 2"]]}}

# Example:
#./create_section.sh -t 1 -l 'My section Label' -i 'my_section_id' -g '0' -c '[{"type":"t","v":[1,"Header h1 Example"]},{"type":"p","v":"Parragraph Example."},{"type":"s","v":"{\n    '\''Code'\'': '\''Block'\'',\n    '\''v'\'': [\n        5,\n        \"Your &lt;b&gt;SNIPPET&lt;br&gt; Example&lt;/b&gt;\"\n    ]\n}"},{"type":"ta","v":{"h":["Header 1", "Header 2"],"r":[["Row 1 Col 1", "Row 1 Col 2"],["Row 2 Col 1", "Row 2 Col 2"]]}}]'

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
    -g|--group_id)
      section_group_id="$2"
      shift 2
      ;;
    -c|--section_content)
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

output=$(python3 create_section.py <<EOF
$section_type
$section_label
$section_id
$section_group_id
$section_content
EOF
)

if [ $? -ne 0 ]; then
  echo "Error:"
  echo "$output"
else
  echo "Success"
fi