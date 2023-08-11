import os
import sys
from PIL import Image

def convert_tiff_resolution(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    tiff_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.tiff') or f.lower().endswith('.tif')]

    for tiff_file in tiff_files:
        input_path = os.path.join(input_folder, tiff_file)
        output_path = os.path.join(output_folder, tiff_file)

        with Image.open(input_path) as img:
            # Convert resolution and save with LZW compression
            img.save(output_path, compression='tiff_lzw', dpi=(300, 300))

        print(f"Converted: {tiff_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    input_folder_name = os.path.basename(input_folder)
    output_folder = os.path.join(os.path.dirname(input_folder), f"{input_folder_name}_300dpi")

    convert_tiff_resolution(input_folder, output_folder)
    print("Conversion complete.")
