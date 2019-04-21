
#   Using Pandas library to provide data structures and data anaylsis tools
import pandas as pd

# Using Numpy library as it consists of multidimensional array objects and a collection of routines for processing those arrays
import numpy as np

# Using seaborn library as it provides a high-level interface for drawing attractive statistical graphics.
import seaborn as sns

import matplotlib.pyplot as plt

# the Iris data sets is being read through the csv file
iris_data = pd.read_csv('data.csv')

iris_data.head()

# Output the results of the data set that is the number of colums and rows
(iris_data.shape)


iris_data['class'].unique()
(iris_data.groupby('class').size())
'Iris-setosa', 'Iris-versicolor', 'Iris-virginica'

iris_data2 = iris_data.set_index("class", drop = False)
'''
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


# Below data is a summary of all data, however it does not distunguish between the class/sprecies of iris
summary = iris_data.describe()
summary = summary.transpose()
print (summary.head())

iris_data.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.gcf().canvas.set_window_title('Iris Attributes Comparsions for all Species')
plt.show()


 
# plotting box graph for sepal length
sns.boxplot(x="class", y="sepallength", data=iris_data)
plt.title('Sepal Length Comparsions')
plt.gcf().canvas.set_window_title('Sepal Length')
plt.show()

sns.boxplot(x="class", y="sepalwidth", data=iris_data)
plt.title('Sepal Width Comparsions')
plt.gcf().canvas.set_window_title('Sepal Width')
plt.show()

sns.boxplot(x="class", y="petallength", data=iris_data)
plt.title('Petal Length Comparsions')
plt.gcf().canvas.set_window_title('Petal Length')
plt.show()

sns.boxplot(x="class", y="petalwidth", data=iris_data)
plt.title('Petal Width Comparsions')
plt.gcf().canvas.set_window_title('Petal Width')
plt.show()


sns.violinplot(x="class", y="sepallength", data=iris_data)
plt.title('Sepal Length Comparsions')
plt.gcf().canvas.set_window_title('Sepal Length')
plt.show()

sns.violinplot(x="class", y="sepalwidth", data=iris_data)
plt.title('Sepal Width Comparsions')
plt.gcf().canvas.set_window_title('Sepal Width')
plt.show()

sns.violinplot(x="class", y="petallength", data=iris_data)
plt.title('Petal Length Comparsions')
plt.gcf().canvas.set_window_title('Petal Length')
plt.show()

sns.violinplot(x="class", y="petalwidth", data=iris_data)
plt.title('Petal Width Comparsions')
plt.gcf().canvas.set_window_title('Petal Width')
plt.show()


dataset = pd.melt(iris_data, "class", var_name="Attrubute")
sns.swarmplot(x="Attrubute", y="value", hue="class", data=dataset)
plt.gcf().canvas.set_window_title('Swarm Plot of all Iris Data')
plt.show()'''



import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

sepallength_min = [4.3, 4.9, 4.9]
sepallength_mean = [5.0, 5.9, 6.6]
sepallength_max = [5.8, 7.0, 7.9]


a=np.array([[4.3, 4.9, 4.9], [5.0, 5.9, 6.6], [5.8, 7.0, 7.9], [2.3, 2.0, 2.2], [3.4, 2.8, 3.0], [4.4, 3.4, 3.8]])
df=pd.DataFrame(a, columns=['Iris-setosa','Iris-versicolor ','Iris-virginica'], index=['sepallength_min','sepallength_mean','sepallength_max', 'sepalwidth_min', 'sepalwidth_mean', 'sepalwidth_max'])

#y_pos = [2,2,2,2,2]
df.plot(kind='bar', rot= 0, figsize= (10,5)) 
plt.gcf().canvas.set_window_title('sepal comparsions')
plt.show()


'''
sepalwidth_min = (2.3, 2.0, 2.2)
sepalwidth_mean = (3.4, 2.8, 3.0)
sepalwidth_max = (4.4, 3.4, 3.8)

petallength_min = (1.0, 3.0, 4.5)
petallength_mean = (1.5, 4.3, 5.5)
petallength_max = (1.9, 5.1, 6.9)

sepalwidth_min = (0.1, 1.0, 1.4)
sepalwidth_mean = (0.2, 1.3, 2.0)
sepalwidth_max = (0.6, 1.8, 2.5)
'''

