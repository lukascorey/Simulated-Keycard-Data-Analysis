#!/usr/bin/env python3

import csv

import pandas as pd 

# https://www.datacamp.com/community/tutorials/decision-tree-classification-python

from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics # Import scikit-learn metrics module for accuracy calculation
from sklearn.tree import export_graphviz # For visualization
from sklearn.externals.six import StringIO  # For visualization
from IPython.display import Image  # For visualization
import pydotplus# For visualization


#read file into pands df with column names 
col_names = ['day', 'day_of_week', 'bass_entered', 'bass_returned', 'lawlib_entered', 'lawlib_returned']
lib_data = pd.read_csv("library_data.csv", header=None, names=col_names)
lib_data.head()

# modify data frame 
lib_data['lawlib_returned'] = (lib_data['lawlib_returned'] >= 250)

# Train on day of week and number of returned books before 6pm
feature_cols = ['day_of_week', 'lawlib_entered']
X = lib_data[feature_cols]
Y = lib_data.lawlib_returned
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.0, random_state=1)

# Create decision tree classifier object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifier
clf = clf.fit(X_train,Y_train)

# predict the response for test, bass saturday 2400 
Y_pred = clf.predict([[4, 450]])

#set message according to prediction
if (Y_pred == False): 
	message = "low-return day."
else: 
	message = "high-return day."


#print message 
print("The Law Library on Thursday with 450 visitorsby 6 p.m. is predicted to be a", message)


#visualize, code from datacamp
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data, filled=True, rounded=True, special_characters=True, feature_names = feature_cols, class_names=['day_of_week', 'lawlib_entered', 'lawlib_returned'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('decision_tree_2.png')
Image(graph.create_png())