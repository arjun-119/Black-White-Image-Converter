# Project Title

Black & White Image Converter

## Description

* Convert the Color & Grayscale Images to Black & White mode
* pillow library used
* OpenCV library used
* Source Image (Input Image) resolution will retain in the converted output image.
* Images types: TIF, PNG types handled

## Getting Started

### Dependencies

* Windows 7

### Installing

* pip install Pillow
* pip install opencv-python

### Executing program

* "value.ini" should present in the tool location and value should be numberic, maximum value 250
* threshold value can be increase (or) decrease based on the input images.
* Run the program
* Ask user to enter the path of the input image file
* Tool will create the Folder "Black&White" in the same directory of input file
* Tool will read the "value.ini" file and get the threshold value
* Tool will convert the images into grayscale mode
* Tool will apply the threshold value in the grayscale mode image
* Convert the Grayscale image to Black & White mode
* The converted Image files will placed in the "Black&White" folder

### Help
* "value.ini" should present in the tool location and value should be numberic, maximum value 250

## Version History

* 0.1
    * Initial Release
