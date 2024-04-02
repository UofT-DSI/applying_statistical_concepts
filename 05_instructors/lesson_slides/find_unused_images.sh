#!/bin/bash

# Ensure two directories are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <image_directory> <markdown_and_ipynb_directory>"
    exit 1
fi

echo "Image directory: $1"
echo "Markdown and IPython Notebook directory: $2"

image_directory="$1"
markdown_and_ipynb_directory="$2"
unused_images=()

# Collect all image filenames from the first folder
echo "Collecting image filenames from $image_directory..."
image_files=$(find "$image_directory" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" \) -exec basename {} \;)

if [ -z "$image_files" ]; then
    echo "No image files found in $image_directory."
    exit 0
fi

# Scan all markdown and ipynb files in the second folder for references to these image filenames
echo "Scanning for references in markdown and IPython Notebook files..."
for image in $image_files; do
    echo "Checking image: $image"
    
    # Initialize a flag to mark if the image is used
    image_used=false

    # Read through all markdown files to check if the image is referenced
    for md_file in "$markdown_and_ipynb_directory"/*.md; do
        if grep -q "$image" "$md_file"; then
            echo "Image $image found in markdown file $md_file"
            image_used=true
            break
        fi
    done

    # # If not found in markdown files, check in ipynb files
    # if [ "$image_used" = false ]; then
    #     for ipynb_file in "$markdown_and_ipynb_directory"/*.ipynb; do
    #         # Use jq to parse the .ipynb file and search for the image name in the "source" fields
    #         if jq -r '.cells[].source[]' "$ipynb_file" 2>/dev/null | grep -q "$image"; then
    #             echo "Image $image found in IPython Notebook file $ipynb_file"
    #             image_used=true
    #             break
    #         fi
    #     done
    # fi

    # If the image is not used in any markdown or ipynb file, add it to the list of unused images
    if [ "$image_used" = false ]; then
        unused_images+=("$image")
    fi
done
