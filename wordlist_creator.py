from PIL import Image
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pyocr
import pyocr.builders
import csv
import re
import os
#external libraries
import class_of_wordlist as CWL

##################################################################################################################################################
##################################################################################################################################################
#//////////////////////////////////////////////////Library for python tesseract//////////////////////////////////////////////////////////////////#
##################################################################################################################################################
##################################################################################################################################################

# get the avialable tool like tesseract
def get_the_available_tool():
	tools = pyocr.get_available_tools()
	if len(tools) == 0:
		print("No OCR tools are available")
		sys.exit()
	# get the first available tool for processing
	tool = tools[0]
	print "Tools used will be : ", tools[0]
	return tool

##################################################################################################################################################


# get the deutch language for further processing
def get_the_lang(tools):
	langs = tools.get_available_languages()
	# check if there is deutch in it or not
	lang = "deu"
	flag_for_lang = 0
	for elements in langs:
		if elements == lang:
			flag_for_lang = 1
	if flag_for_lang == 0:
		print "Deutch language is not available for Tesseract please install the\
			language as -> sudo apt-get install tesseract-ocr-deu"
		sys.exit()
	return lang

##################################################################################################################################################

def word_contents_to_array(image_to_extract_from, lang, tools):	
	# array for storing the data	
	words = []
	x_0 = []
	x_1 = []
	y_0 = []
	y_1 = []
	# getting the word and there information in an array	
	word_boxes = tools.image_to_string(Image.open(image_to_extract_from), lang=lang, 
							builder=pyocr.builders.WordBoxBuilder())
	# moving words from word_boxes to words array
	for different_words in word_boxes:
		words.append(str(different_words.content))
		#print different_words.position[0][0]
		x_0.append(different_words.position[0][0])
		y_0.append(different_words.position[0][1])
		x_1.append(different_words.position[1][0])
		y_1.append(different_words.position[1][1])
			
	return words, x_0, y_0, x_1, y_1

##################################################################################################################################################

# copying all the objects value to an array
# for further writing it to the csv file
def objects_to_array(word, x_0, y_0, x_1, y_1):
	return_arr = []
	return_arr.append([])
	return_arr[0].append("word")
	return_arr[0].append("x0")
	return_arr[0].append("y0")
	return_arr[0].append("x1")
	return_arr[0].append("y1")

	index = 1
	for i in range(0, len(word)):
		return_arr.append([])
		return_arr[index].append(word[i])
		return_arr[index].append(x_0[i])
		return_arr[index].append(y_0[i])
		return_arr[index].append(x_1[i])
		return_arr[index].append(y_1[i])
		index = index + 1
	return return_arr
##################################################################################################################################################

# Writing the array of objects to CSV for weka testing-traing purpose or self evaluation
def write_to_csv(arr, name_of_file):
	name_of_file = name_of_file + '.csv'
	with open(name_of_file, "wb") as f:
		write = csv.writer(f)
		write.writerows(arr)
	return
    
##################################################################################################################################################

def setup(tiff, file_name):
	tools = get_the_available_tool()
	lang = get_the_lang(tools)
	words, x_0, y_0, x_1, y_1 = word_contents_to_array(tiff, lang, tools)
	array_objects = objects_to_array(words, x_0, y_0, x_1, y_1)
	write_to_csv(array_objects, file_name + "_wordlist.csv")
	print "writting", file_name + "_wordlist.csv" 
	#print array_objects
	#print "sizes : ", len(words), " ", len(x_0)
	#print words
	#print coord_word[1]
	

##################################################################################################################################################

if __name__ == "__main__":
	#dir_tiff = "/home/abdullah/Downloads/Data from Ubuntu/PYTHON Scripts/Commercial PNGS/"	
	dir_tiff = raw_input("Please input the Data Directory of Images for BoundingBox Extraction: e.g. /home/abdullah/Downloads/Data from Ubuntu/PYTHON Scripts/CommercialPNGS/:")	
	tiffs = os.listdir(dir_tiff)
	extension = raw_input("Please input the Extension of Image e.g. .PNG: ")
	for tiff in tiffs:
		files = re.split(extension, tiff)[0]
		file_name = files
		tiff_file = dir_tiff + file_name + extension
		setup(tiff_file, file_name)


##################################################################################################################################################
##################################################################################################################################################
#//////////////////////////////////////////////////////////////END OF FILE///////////////////////////////////////////////////////////////////////#
##################################################################################################################################################
##################################################################################################################################################
	
