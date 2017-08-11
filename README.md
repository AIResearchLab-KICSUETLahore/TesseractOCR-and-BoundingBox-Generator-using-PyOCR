# TesseractOCR-and-BoundingBox-Generator-using-PyOCR
This tutorial will guide you throught the installation process of TesseractOCR 3.04.01 with automatically installation 
of Leptonica1.73. Alongside this installation of PyOCR and extracting the wordlist and also how to get bounding box 
using tesseractOCR. 
## Installation of TesseractOCR in Ubuntu
### Installing Depedencies
To run tesseract fine few of the dependencies are necessary which can be installing by simply using following commands.
```
$ sudo apt-get install libpng-dev libjpeg-dev libtiff-dev zlib1g-dev
$ sudo apt-get install gcc g++
$ sudo apt-get install autoconf automake libtool checkinstall
```
### Installing TesseractOCR
To install the tesseractOCR simply write the following command
```
$ sudo apt-get install tesseract-ocr
```
Initially it will come with the -eng language. There 100's of languages available. To download any specific lanaguage
you can use the following template
```
$ sudo apt-get install tesseract-ocr-[lang]
```
for example
```
sudo apt-get install tesseract-ocr-fra
```
or simply download all the langaues pack available by using the command
```
$ sudo apt-get install tesseract-ocr-all
```
Complete list of languages available can be find on this link https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc#languages while it can also be trained for any new language.
### Usage
Usage of testing teseractocr or running is quite simple. You can directly right the output to txt file even. Its template will look alike something
```
$ tesseract [image_path] [file_name]
```
for example my image is test_image.png and I want an output in output_text.txt, then it would look like something this
```
$ tesseract test_image.png output_text.txt
```
## Installation of PyOCR in Ubuntu
PyOCR is a python wrapper for tesseract. It allows you connect programatically to 
tesseract and easily get the wordlist and bounding boxes as per requirment. For installing it simply install it by using following command's
```
$ sudo pip install pyocr  # Python 2.7
$ sudo pip3 install pyocr  # Python 3.X
```
For further information on PyOCR please Visit https://github.com/openpaperwork/pyocr. 

## Conversion of files to Images in Ubuntu
If you have an image you might want to convert it in grayscale for better OCR extraction. While if the data set is not available in Image format. It can easily be converted. For example if the file is in PDF you can simply convert it into any image format like this
```
$ for f in *.pdf; do convert -density 300 "$f" -depth 8 -strip -background white -alpha off -threshold 85% "$f.PNG"; done
```
For convert command imagemagick is required which can easily be installed as shown
```
$ sudo apt-get install imagemagick
```
If you file is in image format and you want to convert it into grayscale you can simply use this statement
```
$ convert source.jpg -colorspace Gray destination.jpg (true grayscale only)
$ convert source.jpg -monochrome destination.jpg (true black and white)
$ convert source.jpg -separate destination.jpg (separate into gray channels)
```
## Extracting BoundingBox into CSV format using TesseractOCR and PyOCR

