import sys
import os
from PIL import Image
import cv2
import re
import glob
import wand.image

# pillow library used
# OpenCV library used
# ImageMagick (wand) library used

# *** Tool executing procedure ***
# "value.ini" should present in the tool location and value should be numeric, maximum value 250
# get the Input file directory
# Folder "Black-White" will be created in the same directory of input file
# Tool reads the "value.ini" file and get the threshold value
# convert the images into grayscale mode
# apply the threshold value in the grayscale mode image
# convert the Grayscale image to Black & White mode
# The converted Image files will be placed in the "Black-White" folder
# Converted TIFF Image is a lower version (4.0), so used ImageMagick and saved to TIFF Version 5.0

print("\n TIF, PNG, JPG: Black & White mode Conversion \n")

filepath = input("Enter the Input Image file path: ")
output_directory = "Black-White"
output = os.path.join(filepath, output_directory)

if not os.path.exists(output):
    os.mkdir(output)

value = "value.ini"  # Threshold value should update in the INI file.

if not os.path.exists(value):  # check if the value.ini file is present
    print("\n value.ini file is missing")
    sys.exit(1)

# open the "value.ini" file and read the threshold value
with open(value) as f:  # open the ini file
    str1 = f.read()  # read the ini file
    val = int(str1)

def process_image(fname):
    input_image = fname
    image = cv2.imread(input_image)
    name = os.path.basename(fname)
    print(name)

    # get the Image DPI value from the Input images
    image1 = Image.open(input_image)
    img_dpi = str(image1.info.get('dpi', (72, 72)))
    patn = re.sub(r"[\(\)]", "", img_dpi)
    sp = patn.split(",")[0]
    dpi_val = round(float(sp))
    comp_img = str(image1.info.get('compression', ''))

    # convert to Grayscale format
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # applying threshold
    (t, blackAndWhiteImage) = cv2.threshold(grayImage, val, 255, cv2.THRESH_BINARY)
    save_image = Image.fromarray(blackAndWhiteImage)

    # convert to Black & White Mode
    bw_conv = save_image.convert('1')
    bw_conv.save(os.path.join(output, "del" + name), dpi=(dpi_val, dpi_val), compression=comp_img)
    name1 = os.path.join(output, "del" + name)

    # Pillow converted output is a lower version tiff image, so use the ImageMagick library and convert to TIFF version 5.0
    with wand.image.Image(filename=name1) as img:
        img.save(filename=os.path.join(output, name))
        os.remove(os.path.join(output, "del" + name))

# Process .tif files
for fname in glob.glob(os.path.join(filepath, "*.tif")):
    process_image(fname)

# Process .png files
for fname in glob.glob(os.path.join(filepath, "*.png")):
    process_image(fname)

# Process .jpg files
for fname in glob.glob(os.path.join(filepath, "*.jpg")):
    process_image(fname)

print("\n\n *** Process Completed *** \n")
