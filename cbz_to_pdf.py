#!/usr/bin/env python3

import os
import shutil
from PIL import Image
import zipfile

# Define directories
current_dir = os.path.dirname(os.path.abspath(__file__))
old_dir = os.path.join(current_dir, 'old')

# Create 'old' directory if it doesn't exist
if not os.path.exists(old_dir):
    os.makedirs(old_dir)

# Function to convert CBZ to PDF
def cbz_to_pdf(cbz_path, pdf_path):
    with zipfile.ZipFile(cbz_path, 'r') as archive:
        image_files = sorted([name for name in archive.namelist() if name.lower().endswith(('jpg', 'jpeg', 'png'))])

        images = [Image.open(archive.open(image_file)) for image_file in image_files]
        if images:
            images[0].save(pdf_path, save_all=True, append_images=images[1:], resolution=100.0, quality=95)

# Process each CBZ/CBR file in the directory
for filename in os.listdir(current_dir):
    if filename.lower().endswith(('.cbz', '.cbr')):
        file_path = os.path.join(current_dir, filename)
        pdf_path = os.path.join(current_dir, filename.rsplit('.', 1)[0] + '.pdf')
        cbz_to_pdf(file_path, pdf_path)
        shutil.move(file_path, os.path.join(old_dir, filename))
