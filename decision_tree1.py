#!/usr/bin/env python3

import csv

import pandas as pd 

# https://www.datacamp.com/community/tutorials/decision-tree-classification-python
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics # Import scikit-learn metrics module for accuracy calculation
from sklearn.tree import export_graphviz #for visualization
from sklearn.externals.six import StringIO  #for visualization
from IPython.display import Image  #for visualization
import graphviz #for visualization
import pydotplus #for visualization

# set column names for pandas df 
col_names = ['day', 'day_of_week', 'bass_entered', 'bass_returned', 'lawlib_entered', 'lawlib_returned']

# Read csv file into pandas df 
lib_data = pd.read_csv("library_data.csv", header=None, names=col_names)
lib_data.head()

# modify data frame 
lib_data['bass_returned'] = (lib_data['bass_returned'] >=250)

# Set feature columns and return 
feature_cols = ['day_of_week', 'bass_entered']
X = lib_data[feature_cols]
Y = lib_data.bass_returned

# put all data into the training data, no test data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.0, random_state=1)

# Create decision tree classifier object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifier
clf = clf.fit(X_train, Y_train)

# predict the response for test, bass saturday 2400 
Y_pred = clf.predict([[6, 2400]])

# make message correspond with prediction
if (Y_pred == False): 
	message = "low-return day."
else: 
	message = "high-return day."

#print message 
print("Bass on a Saturday with 2400 visitors by 6 p.m. is predicted to be a", message)

#visualize, code from datacamp link above
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data, filled=True, rounded=True, special_characters=True, feature_names = feature_cols, class_names=['day_of_week','bass_entered', 'bass_returned'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('decision_tree_1.png')
Image(graph.create_png())