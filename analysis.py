
#   Using Pandas library to provide data structures and data anaylsis tools
import pandas as pd

# Using Numpy library as it consists of multidimensional array objects and a collection of routines for processing those arrays
import numpy as np

# Using seaborn library as it provides a high-level interface for drawing attractive statistical graphics.
import seaborn as sns

# Using matplotlib.pyplot library is useful for plotting graphs
import matplotlib.pyplot as plt

#Dataframe is a 2-dimensional labeled data structure with columns of potentially different types.  
from pandas import DataFrame

# the Iris data sets is being read through the csv file
iris_data = pd.read_csv('data.csv')

# Output the results of the data set that is the number of colums and rows
print ('Number of Rows and Colums in data set:', iris_data.shape)

# Analyses the Iris data set by class and size and prints out the number of data available per class/species
iris_data['class'].unique()
print (iris_data.groupby('class').size())
'Iris-setosa', 'Iris-versicolor', 'Iris-virginica'

iris_data2 = iris_data.set_index("class", drop = False)

# Prints a table with the summary of the class, count, mean, standard deviation, minimum, 25%, 50%, 75% and maximum values.
summary = iris_data.describe()
summary = summary.transpose()
print(summary.head())

#Setting the formation and title layout of the graph
iris_data.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.gcf().canvas.set_window_title('Summary of the Iris Flower Data Set for all Species') # Prunts title in pop up box
plt.title('Summary of the Iris Flower Data Set',x=0, y=2.3)
plt.show() # Prints Graph

#Calculated the min sepal length for each of the species
sepallength_min = [iris_data2.loc["Iris-setosa","sepallength"].min(), iris_data2.loc["Iris-versicolor","sepallength"].min(), iris_data2.loc["Iris-virginica","sepallength"].min()]
#Calculated the mean sepal length for each of the species
sepallength_mean = [iris_data2.loc["Iris-setosa","sepallength"].mean(), iris_data2.loc["Iris-versicolor","sepallength"].mean(),iris_data2.loc["Iris-virginica","sepallength"].mean()]
#Calculated the max sepal length for each of the species
sepallength_max = [iris_data2.loc["Iris-setosa","sepallength"].max(), iris_data2.loc["Iris-versicolor","sepallength"].max(), iris_data2.loc["Iris-virginica","sepallength"].max()]

#Calculated the min sepal width for each of the species
sepalwidth_min = [iris_data2.loc["Iris-setosa","sepalwidth"].min(), iris_data2.loc["Iris-versicolor","sepalwidth"].min(), iris_data2.loc["Iris-virginica","sepalwidth"].min()]
#Calculated the mean sepal width for each of the species
sepalwidth_mean = [iris_data2.loc["Iris-setosa","sepalwidth"].mean(), iris_data2.loc["Iris-versicolor","sepalwidth"].mean(), iris_data2.loc["Iris-virginica","sepalwidth"].mean()]
#Calculated the max sepal width for each of the species
sepalwidth_max = [iris_data2.loc["Iris-setosa","sepalwidth"].max(), iris_data2.loc["Iris-versicolor","sepalwidth"].max(), iris_data2.loc["Iris-virginica","sepalwidth"].max()]

#Calculated the min petal length for each of the species
petallength_min = [iris_data2.loc["Iris-setosa","petallength"].min(), iris_data2.loc["Iris-versicolor","petallength"].min(), iris_data2.loc["Iris-virginica","petallength"].min()]
#Calculated the mean petal length for each of the species
petallength_mean =[iris_data2.loc["Iris-setosa","petallength"].mean(), iris_data2.loc["Iris-versicolor","petallength"].mean(), iris_data2.loc["Iris-virginica","petallength"].mean()]
#Calculated the max petal length for each of the species
petallength_max = [iris_data2.loc["Iris-setosa","petallength"].max(), iris_data2.loc["Iris-versicolor","petallength"].max(), iris_data2.loc["Iris-virginica","petallength"].max()]

#Calculated the min petal width for each of the species
petalwidth_min = [iris_data2.loc["Iris-setosa","petalwidth"].min(), iris_data2.loc["Iris-versicolor","petalwidth"].min(), iris_data2.loc["Iris-virginica","petalwidth"].min()]
#Calculated the mean petal width for each of the species
petalwidth_mean = [iris_data2.loc["Iris-setosa","petalwidth"].mean(), iris_data2.loc["Iris-versicolor","petalwidth"].mean(), iris_data2.loc["Iris-virginica","petalwidth"].mean()]
#Calculated the max petal width for each of the species
petalwidth_max = [iris_data2.loc["Iris-setosa","petalwidth"].max(), iris_data2.loc["Iris-versicolor","petalwidth"].max(), iris_data2.loc["Iris-virginica","petalwidth"].max()]

#Setting the parameters for plotting a bar chart, setting columns, labels, graph size and pop up chart name
a=np.array([sepallength_min, sepallength_mean, sepallength_max, sepalwidth_min, sepalwidth_mean, sepalwidth_max])
df=pd.DataFrame(a, columns=['Iris-setosa','Iris-versicolor ','Iris-virginica'], index=['sepallength_min','sepallength_mean','sepallength_max', 'sepalwidth_min', 'sepalwidth_mean', 'sepalwidth_max'])

#Plotting the data for Sepal Comparsions
df.plot(kind='bar', rot= 0, figsize= (10,5)) 
plt.gcf().canvas.set_window_title('Sepal Comparsions')
plt.title('Sepal Comparsions',x=0.5, y=1)
plt.show()

#Setting the parameters for plotting a bar chart, setting columns, labels, graph size and pop up chart name
b=np.array([petallength_min, petallength_mean, petallength_max, petalwidth_min, petalwidth_mean, petalwidth_max])
df=pd.DataFrame(b, columns=['Iris-setosa','Iris-versicolor ','Iris-virginica'], index=['petallength_min','petallength_mean','petallength_max', 'petalwidth_min', 'petalwidth_mean', 'petalwidth_max'])


#Plotting the data for Petal Comparsions
df.plot(kind='bar', rot= 0, figsize= (10,5)) 
plt.gcf().canvas.set_window_title('Petal Comparsions')
plt.title('Petal Comparsions',x=0.5, y=1)
plt.show()

# plotting box graph for Sepal Length
sns.boxplot(x="class", y="sepallength", data=iris_data)
plt.title('Sepal Length Comparsions',x=0.5, y=1)
plt.gcf().canvas.set_window_title('Sepal Length')
plt.show()

# plotting box graph for Sepal Width
sns.boxplot(x="class", y="sepalwidth", data=iris_data)
plt.title('Sepal Width Comparsions')
plt.gcf().canvas.set_window_title('Sepal Width')
plt.show()

# plotting box graph for Petal Length
sns.boxplot(x="class", y="petallength", data=iris_data)
plt.title('Petal Length Comparsions')
plt.gcf().canvas.set_window_title('Petal Length')
plt.show()

# plotting box graph for Petal Width
sns.boxplot(x="class", y="petalwidth", data=iris_data)
plt.title('Petal Width Comparsions')
plt.gcf().canvas.set_window_title('Petal Width')
plt.show()

# plotting a violin graph and setting graph parameters for Sepal Length Comparsions
sns.violinplot(x="class", y="sepallength", data=iris_data)
plt.title('Sepal Length Comparsions')
plt.gcf().canvas.set_window_title('Sepal Length')
plt.show()

# plotting a violin graph and setting graph parameters for Sepal Width Comparsions
sns.violinplot(x="class", y="sepalwidth", data=iris_data)
plt.title('Sepal Width Comparsions')
plt.gcf().canvas.set_window_title('Sepal Width')
plt.show()

# plotting a violin graph and setting graph parameters for Petal Length Comparsions
sns.violinplot(x="class", y="petallength", data=iris_data)
plt.title('Petal Length Comparsions')
plt.gcf().canvas.set_window_title('Petal Length')
plt.show()

# plotting a violin graph and setting graph parameters for Petal Width Comparsions
sns.violinplot(x="class", y="petalwidth", data=iris_data)
plt.title('Petal Width Comparsions')
plt.gcf().canvas.set_window_title('Petal Width')
plt.show()

#simplifying the data set to plot a swarmplot that shows the data without over lapping the data points 
dataset = pd.melt(iris_data, "class", var_name="Attribute")
sns.swarmplot(x="Attribute", y="value", hue="class", data=dataset)
plt.title('Swarm Plot of all Iris Data')
plt.gcf().canvas.set_window_title('Swarm Plot of all Iris Data')
plt.show()


# Ploting a scatter plot
sns.pairplot(iris_data, hue="class", height=2, aspect =1)
plt.gcf().canvas.set_window_title('Pair Plot for all Species')
#show plot
plt.show()

# Ploting a scatter plot with regression models
sns.pairplot(iris_data, kind="reg",hue="class", height=2, aspect =1)
plt.gcf().canvas.set_window_title('Pair Plot for all Species')
#show plot
plt.show()

# Ploting a Hexagonal Bin Plot
sns.jointplot(x="sepallength", y="sepalwidth", data=iris_data, height=5,ratio=10, kind='hex',color='green')
plt.gcf().canvas.set_window_title('Hexagonal Bin Plot of Iris Data')
plt.show()