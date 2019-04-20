'''
import pandas as pd

iris_data = pd.read_csv('data.csv')
iris_data2 = iris_data.set_index("class", drop = False)
print ("Iris-setosa max sepal length is: " , iris_data2.loc["Iris-setosa","sepallength"].max())
print ("Iris-setosa mean sepal length is: " , iris_data2.loc["Iris-setosa","sepallength"].mean())
print ("Iris-setosa min sepal length is: " , iris_data2.loc["Iris-setosa","sepallength"].min())
print ("")
print ("Iris-setosa max sepal width is: " , iris_data2.loc["Iris-setosa","sepalwidth"].max())
print ("Iris-setosa mean sepal width is: " , iris_data2.loc["Iris-setosa","sepalwidth"].mean())
print ("Iris-setosa min sepal width is: " , iris_data2.loc["Iris-setosa","sepalwidth"].min())
print ("")
print ("Iris-setosa max petal length is: " , iris_data2.loc["Iris-setosa","petallength"].max())
print ("Iris-setosa mean petal length is: " , iris_data2.loc["Iris-setosa","petallength"].mean())
print ("Iris-setosa min petal length is: " , iris_data2.loc["Iris-setosa","petallength"].min())
print ("")
print ("Iris-setosa max petal width is: " , iris_data2.loc["Iris-setosa","petalwidth"].max())
print ("Iris-setosa mean petal width is: " , iris_data2.loc["Iris-setosa","petalwidth"].mean())
print ("Iris-setosa min petal width is: " , iris_data2.loc["Iris-setosa","petalwidth"].min())
print ("")
print ("The shortest sepal length for all flower type is: " , iris_data2["sepallength"].min())
print ("The shortest sepal width for all flower type is: " , iris_data2["sepalwidth"].min())
print ("The shortest petal length for all flower type is: " , iris_data2["petallength"].min())
print ("The shortest petal width for all flower type is: " , iris_data2["petalwidth"].min())
'''
#   Using Pandas library to provide data structures and data anaylsis tools
import pandas as pd

# Using Numpy library as it consists of multidimensional array objects and a collection of routines for processing those arrays
import numpy as np

# Using seaborn library as it provides a high-level interface for drawing attractive statistical graphics.
import seaborn as sns

# the Iris data sets is being read through the csv file
iris_data = pd.read_csv('data.csv')

# Output the results of the data set that is the number of colums and rows
print (iris_data.shape)





