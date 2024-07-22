# CBZ to PDF Converter

This Python script converts `.cbz` and `.cbr` files to PDF format and moves the original files to a folder named `old` within the same directory.

## Requirements

- **Python 3**: Ensure that Python 3 is installed on your system.
- **Pillow**: Python Imaging Library to handle image processing.

## Installation

1. **Install Pillow Library**:
   Open a terminal and install Pillow using pip:
    ```bash
    pip install pillow
    ```
2. **Clone the Repository**:
   Open a terminal and clone the repository from GitHub:
    ```bash
    git clone https://github.com/empr0r/CBZ-to-pdf.git
    ```

## Usage

1. **Prepare Your Directory**:
   - Drop the `cbz_to_pdf.py` script into the directory containing your `.cbz` or `.cbr` files.

2. **Set Permissions**:
   - Open a terminal and navigate to the directory where you placed the script.
   - Make the script executable by running:
     ```bash
     chmod +x cbz_to_pdf.py
     ```

3. **Run the Script**:
   - Execute the script by running:
     ```bash
     ./cbz_to_pdf.py
     ```

   This will process all `.cbz` and `.cbr` files in the directory, convert them to PDF, and move the original files to a folder called `old`.

## License

**This project is licensed under the MIT License. See the LICENSE file for details.**

## Troubleshooting

- **ModuleNotFoundError: No module named 'PIL':**
  Ensure you have installed the Pillow library.

- **Permission Denied:**
  Make sure you have executed the `chmod +x cbz_to_pdf.py` command before running the script.
