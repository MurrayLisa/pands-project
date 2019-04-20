
#   Using Pandas library to provide data structures and data anaylsis tools
import pandas as pd

# Using Numpy library as it consists of multidimensional array objects and a collection of routines for processing those arrays
import numpy as np

# Using seaborn library as it provides a high-level interface for drawing attractive statistical graphics.
import seaborn as sns

# the Iris data sets is being read through the csv file
iris_data = pd.read_csv('data.csv')

# Output the results of the data set that is the number of colums and rows
(iris_data.shape)

iris_data['class'].unique()
print(iris_data.groupby('class').size())
'Iris-setosa', 'Iris-versicolor', 'Iris-virginica'

iris_data2 = iris_data.set_index("class", drop = False)

print ("Iris-setosa max sepal length is: " , iris_data2.loc["Iris-setosa","sepallength"].max())
print ("Iris-setosa mean sepal length is: " , iris_data2.loc["Iris-setosa","sepallength"].mean())
print ("Iris-setosa min sepal length is: " , iris_data2.loc["Iris-setosa","sepallength"].min())

print ("Iris-setosa max sepal width is: " , iris_data2.loc["Iris-setosa","sepalwidth"].max())
print ("Iris-setosa mean sepal width is: " , iris_data2.loc["Iris-setosa","sepalwidth"].mean())
print ("Iris-setosa min sepal width is: " , iris_data2.loc["Iris-setosa","sepalwidth"].min())

print ("Iris-setosa max petal length is: " , iris_data2.loc["Iris-setosa","petallength"].max())
print ("Iris-setosa mean petal length is: " , iris_data2.loc["Iris-setosa","petallength"].mean())
print ("Iris-setosa min petal length is: " , iris_data2.loc["Iris-setosa","petallength"].min())

print ("Iris-setosa max petal width is: " , iris_data2.loc["Iris-setosa","petalwidth"].max())
print ("Iris-setosa mean petal width is: " , iris_data2.loc["Iris-setosa","petalwidth"].mean())
print ("Iris-setosa min petal width is: " , iris_data2.loc["Iris-setosa","petalwidth"].min())

print ("Iris-versicolor max sepal length is: " , iris_data2.loc["Iris-versicolor","sepallength"].max())
print ("Iris-versicolor mean sepal length is: " , iris_data2.loc["Iris-versicolor","sepallength"].mean())
print ("Iris-versicolor min sepal length is: " , iris_data2.loc["Iris-versicolor","sepallength"].min())

print ("Iris-versicolor max sepal width is: " , iris_data2.loc["Iris-versicolor","sepalwidth"].max())
print ("Iris-versicolor mean sepal width is: " , iris_data2.loc["Iris-versicolor","sepalwidth"].mean())
print ("Iris-versicolor min sepal width is: " , iris_data2.loc["Iris-versicolor","sepalwidth"].min())

print ("Iris-versicolor max petal length is: " , iris_data2.loc["Iris-versicolor","petallength"].max())
print ("Iris-versicolor mean petal length is: " , iris_data2.loc["Iris-versicolor","petallength"].mean())
print ("Iris-versicolor min petal length is: " , iris_data2.loc["Iris-versicolor","petallength"].min())

print ("Iris-versicolor max petal width is: " , iris_data2.loc["Iris-versicolor","petalwidth"].max())
print ("Iris-versicolor mean petal width is: " , iris_data2.loc["Iris-versicolor","petalwidth"].mean())
print ("Iris-versicolor min petal width is: " , iris_data2.loc["Iris-versicolor","petalwidth"].min())

print ("Iris-virginica max sepal length is: " , iris_data2.loc["Iris-virginica","sepallength"].max())
print ("Iris-virginica mean sepal length is: " , iris_data2.loc["Iris-virginica","sepallength"].mean())
print ("Iris-virginica min sepal length is: " , iris_data2.loc["Iris-virginica","sepallength"].min())

print ("Iris-virginica max sepal width is: " , iris_data2.loc["Iris-virginica","sepalwidth"].max())
print ("Iris-virginica mean sepal width is: " , iris_data2.loc["Iris-virginica","sepalwidth"].mean())
print ("Iris-virginica min sepal width is: " , iris_data2.loc["Iris-virginica","sepalwidth"].min())

print ("Iris-virginica max petal length is: " , iris_data2.loc["Iris-virginica","petallength"].max())
print ("Iris-virginica mean petal length is: " , iris_data2.loc["Iris-virginica","petallength"].mean())
print ("Iris-virginica min petal length is: " , iris_data2.loc["Iris-virginica","petallength"].min())

print ("Iris-virginica max petal width is: " , iris_data2.loc["Iris-virginica","petalwidth"].max())
print ("Iris-virginica mean petal width is: " , iris_data2.loc["Iris-virginica","petalwidth"].mean())
print ("Iris-virginica min petal width is: " , iris_data2.loc["Iris-virginica","petalwidth"].min())


