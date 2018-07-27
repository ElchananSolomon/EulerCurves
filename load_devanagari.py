# -*- coding: utf-8 -*-
"""
Loads Devanagari Data

Parameters


Loads
-----
train_letter_dictionary -- a dictionary with character names as keys and arrays of training images as objects
test_letter_dictionary -- a dictionary with character names as keys and arrays of testing images ad objects

devan_train_figures -- an array of training images for all characters
devan_test_figures -- an array of testing images for all characters

devan_train_labels -- an array of character labels matching devan_train_figures
devan_test_labels -- an array of character labes matching devan_tests_figures

@author: Elchanan Solomon
"""
#Specify size of training and testing set
training_size = 5
testing_size = 5

# Load Devanagari Data
from os import listdir
import imageio
#Specify the file path where the data sets are stored
mypath_train = "C:/Users/Elchanan/Downloads/DevanagariHandwrittenCharacterDataset/DevanagariHandwrittenCharacterDataset/train"
#Find the 36 Devanagari letters in the file
train_letter_filenames = [f for f in listdir(mypath_train) if f.startswith('character')]
#We'll use these letter names as the keys of a dictionary
train_letter_dictionary = {}
#We select some subset of letters to store as data
for file in train_letter_filenames[:]:
    #The dictionary value will be an array of images
    train_letter_dictionary[file] = []
    #We'll set our new path to be the folder corresponding to this letter
    mypath_train_char = mypath_train + "/" + file
    #We collect all the filenames in this folder
    char_letter_filenames = [char for char in listdir(mypath_train_char)]
    #For some subset of characters in the folder
    for char in char_letter_filenames[0:training_size]:
        #We set the path to be the location of that character
        mypath_train_char_num = mypath_train_char + "/" + char
        #We read in the image
        new_char = imageio.imread(mypath_train_char_num)
        #and store it in the dictionary
        (train_letter_dictionary[file]).append(new_char)

#We will store the keys for later convenience    
train_letter_keys = list(train_letter_dictionary.keys())

#Now, we repeat all this for the testing data

#Specify the file path where the data sets are stored
mypath_test = "C:/Users/Elchanan/Downloads/DevanagariHandwrittenCharacterDataset/DevanagariHandwrittenCharacterDataset/test"
#Find the 36 Devanagari letters in the file
test_letter_filenames = [f for f in listdir(mypath_test) if f.startswith('character')]
#We'll use these letter names as the keys of a dictionary
test_letter_dictionary = {}
#We select some subset of letters to store as data
for file in test_letter_filenames[:]:
    #The dictionary value will be an array of images
    test_letter_dictionary[file] = []
    #We'll set our new path to be the folder corresponding to this letter
    mypath_test_char = mypath_test + "/" + file
    #We collect all the filenames in this folder
    char_letter_filenames = [char for char in listdir(mypath_test_char)]
    #For some subset of characters in the folder
    for char in char_letter_filenames[0:testing_size]:
        #We set the path to be the location of that character
        mypath_test_char_num = mypath_test_char + "/" + char
        #We read in the image
        new_char = imageio.imread(mypath_test_char_num)
        #and store it in the dictionary
        (test_letter_dictionary[file]).append(new_char)
        
#We will store the keys for later convenience    
test_letter_keys = list(test_letter_dictionary.keys())      

#Let us convert our dictionary of training images into an array
devan_train_figures = []
devan_train_labels = []
#For every letter...
for k in train_letter_keys:
    #For each image of that letter...
    for im in train_letter_dictionary[k]:
        #Add it to our array and store its character label
        devan_train_figures.append(im)
        devan_train_labels.append(k)

#Let us convert our dictionary of testing images into an array    
devan_test_figures = []
devan_test_labels = []
#For every letter...
for k in test_letter_keys:
    #For each image of that letter...
    for im in test_letter_dictionary[k]:
        #Add it to our array and store its character label
        devan_test_figures.append(im)
        devan_test_labels.append(k)    

  
