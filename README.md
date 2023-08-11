# TIFF Resolution Conversion Script

This Python script takes a folder path as an argument, converts every TIFF file in that folder from a resolution of 600 pixels per inch to 300 pixels per inch, and saves the output TIFFs with LZW compression. The converted TIFFs are created in a new folder adjacent to the original one, named by adding '\_300dpi' to the end of the original folder's name.

## Requirements

- Python 3
- Pillow library (for image manipulation)

## Usage

1. Clone this repository or download the `convert_resolution.py` script.
2. Install the Pillow library by running: `pip install Pillow`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the `convert_resolution.py` script.
5. Run the script by providing the path to the folder containing TIFF files as an argument:

   ```shell
   python convert.py /path/to/original_folder
   ```

Replace `/path/to/original_folder` with the actual path to the folder containing your TIFF files.

The script will process the TIFF files, convert their resolution, and save them with LZW compression in a new folder named after the original folder, with '\_300dpi' appended to it.

---

Author - [Lukáš Václavek](http://lukasvaclavek.eu/)
