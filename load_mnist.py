# -*- coding: utf-8 -*-
"""
Loads MNIST data from csv file.

Parameters
---------
training_size,testing_size -- size of training and testing sets

Loads 
------
mnist_train_data -- array of 28x28 greyscale training images 
mnist_test_data -- array of 28x28 greyscale testing images

mnist_train_labels -- array of labels for training data
mnist_test_labels -- array of labels for testing data



@author: Elchanan Solomon


"""

#Load MNIST training and testing data sets
import pandas as pd
import numpy as np

#These variables control the size of the training and testing subsets
training_size = 250
testing_size = 100

#Read in the 60,000 x 785 CSV file
df=pd.read_csv('C:/Users/Elchanan/Downloads/mnist_train.csv', sep=',',header=None)
#Convert it to an numpy array
train = df.values
#The CSV array consists of 60,000 training figures. Each figure is stored as a list of 
#785 elements, the first of which records the label. Let's take the first 200...
mnist_train_labels = train[:training_size,0]
#The remaining 784 elements are a vectorization of a 28x28 greyscale image
mnist_train_vectors = train[:,1:]
#We will store the training data as an array of figures
mnist_train_data = []
#For some subset of the figures, we reshape them to be 28x28 and put them in our array
for i in range(training_size):
    mnist_train_data.append(np.reshape(mnist_train_vectors[i,:], (28, 28)))
    
#Read in the 10,000 x 785 CSV file
df=pd.read_csv('C:/Users/Elchanan/Downloads/mnist_test.csv', sep=',',header=None)
#Convert it to an numpy array
test = df.values
#The CSV array consists of 10,000 testing figures. Each figure is stored as a list of 
#785 elements, the first of which records the label. Let's take the first 200...
mnist_test_labels = test[:testing_size,0]
#The remaining 784 elements are a vectorization of a 28x28 greyscale image
mnist_test_vectors = test[:,1:]
#We will store the testing data as an array of figures
mnist_test_data = []
#For some subset of the figures, we reshape them to be 28x28 and put them in our array
for i in range(testing_size):
    mnist_test_data.append(np.reshape(mnist_test_vectors[i,:], (28, 28)))
