
"""
Analyzing and Classifying Devanagari Characters Dataset using euler characteristic curves

@author: Elchanan
"""

  
import ECC
import numpy as np
import matplotlib.pyplot as plt
#Sample 8 directions on the unit circle
directions = [(1,0),(0,1),(1/1.414,1/1.414)]
#directions = [(np.cos(x),np.sin(x)) for x in np.linspace(0,np.pi/2,16)]
#directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1),(2,1),(2,-1),(-2,1),(-2,-1)]
#directions = [(np.cos(x),np.sin(x)) for x in np.linspace(0,np.pi,4)]

#Predict labels for 100 test images
labels = ECC.predict_labels(devan_train_figures,devan_train_labels,devan_test_figures,directions,1)
#Display the score
print('Accuracy on the test set: ' + str(sum(np.array(labels) == np.array(devan_test_labels))/(len(devan_test_figures) + 0.0)) +'%' )
