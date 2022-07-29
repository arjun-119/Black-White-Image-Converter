import sys
import os
from PIL import Image
import cv2
import re
import glob

# pillow library used
# OpenCV library used

# *** Tool executing procedure ***
# "value.ini" should present in the tool location and value should be numberic, maximum value 250
# get the Input file directory
# Folder "Black&White" will be created in the same directory of input file
# Tool read the "value.ini" file and get the threshold value
# convert the images into grayscale mode
# apply the threshold value in the grayscale mode image
# convert the Grayscale image to Black & White mode
# The converted Image files will placed in the "Black&White" folder

print("\n TIF, PNG: Black & White mode Conversion \n")

filepath = input("Enter the Input Image file path: ")
output_directory = "Black&White"
output = filepath + "/" + output_directory + "/"

if os.path.exists(output):
    pass
else:
    os.mkdir(output)

value = "value.ini"  # Threshold value should update in the INI file.

if os.path.exists(value): # check the value.ini file present
    pass
else:
    print("\n value.ini file is missing")

# open the "value.ini" file and read the threshold value
with open(value) as f:   # open the ini file
	str1 = f.read()       # read the ini file
	val = int(str1)

for fname in glob.glob(filepath + "/" + "*.tif"):
	input_image = fname
	image = cv2.imread(input_image)
	filename = os.path.basename(fname)
	print(filename)

	# get the Image DPI value from the Input images
	image1 = Image.open(input_image)
	img_dpi = str(image1.info['dpi'])
	patn = re.sub(r"[\(\)]", "", img_dpi)
	sp = patn.split(",")[0]
	dpi_val = round(float(sp))

	# convert to Grayscale format
	grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# applying threshold
	(t, blackAndWhiteImage) = cv2.threshold(grayImage, val, 255, cv2.THRESH_BINARY)
	save_image = Image.fromarray(blackAndWhiteImage)

	# convert to Black & White Mode
	bw_conv = save_image.convert('1')
	bw_conv.save(output + filename, dpi=(dpi_val,dpi_val))

for fname in glob.glob(filepath + "/" + "*.png"):
	input_image = fname
	image = cv2.imread(input_image)
	filename = os.path.basename(fname)
	print(filename)

	# get the Image DPI value from the Input images
	image1 = Image.open(input_image)
	img_dpi = str(image1.info['dpi'])
	patn = re.sub(r"[\(\)]", "", img_dpi)
	sp = patn.split(",")[0]
	dpi_val = round(float(sp))

	# convert to Grayscale format
	grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# applying threshold
	(t, blackAndWhiteImage) = cv2.threshold(grayImage, val, 255, cv2.THRESH_BINARY)
	save_image = Image.fromarray(blackAndWhiteImage)

	# convert to Black & White Mode
	bw_conv = save_image.convert('1')
	bw_conv.save(output + filename, dpi=(dpi_val,dpi_val))

print("\n\n *** Process Completed *** \n")