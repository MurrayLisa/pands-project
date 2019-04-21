
#   Using Pandas library to provide data structures and data anaylsis tools
import pandas as pd

# Using Numpy library as it consists of multidimensional array objects and a collection of routines for processing those arrays
import numpy as np

# Using seaborn library as it provides a high-level interface for drawing attractive statistical graphics.
import seaborn as sns

import matplotlib.pyplot as plt


from pandas import DataFrame


# the Iris data sets is being read through the csv file
iris_data = pd.read_csv('data.csv')
'''
iris_data.head()

# Output the results of the data set that is the number of colums and rows
iris_data.shape)


iris_data['class'].unique()
(iris_data.groupby('class').size())
'Iris-setosa', 'Iris-versicolor', 'Iris-virginica'
'''
iris_data2 = iris_data.set_index("class", drop = False)

'''# Below data is a summary of all data, however it does not distunguish between the class/sprecies of iris
summary = iris_data.describe()
summary = summary.transpose()
print (summary.head())

iris_data.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.gcf().canvas.set_window_title('Iris Attributes Comparsions for all Species')
plt.show()

'''


sepallength_min = [iris_data2.loc["Iris-setosa","sepallength"].min(), iris_data2.loc["Iris-versicolor","sepallength"].min(), iris_data2.loc["Iris-virginica","sepallength"].min()]
sepallength_mean = [iris_data2.loc["Iris-setosa","sepallength"].mean(), iris_data2.loc["Iris-versicolor","sepallength"].mean(),iris_data2.loc["Iris-virginica","sepallength"].mean()]
sepallength_max = [iris_data2.loc["Iris-setosa","sepallength"].max(), iris_data2.loc["Iris-versicolor","sepallength"].max(), iris_data2.loc["Iris-virginica","sepallength"].max()]

sepalwidth_min = [iris_data2.loc["Iris-setosa","sepalwidth"].min(), iris_data2.loc["Iris-versicolor","sepalwidth"].min(), iris_data2.loc["Iris-virginica","sepalwidth"].min()]
sepalwidth_mean = [iris_data2.loc["Iris-setosa","sepalwidth"].mean(), iris_data2.loc["Iris-versicolor","sepalwidth"].mean(), iris_data2.loc["Iris-virginica","sepalwidth"].mean()]
sepalwidth_max = [iris_data2.loc["Iris-setosa","sepalwidth"].max(), iris_data2.loc["Iris-versicolor","sepalwidth"].max(), iris_data2.loc["Iris-virginica","sepalwidth"].max()]

petallength_min = [iris_data2.loc["Iris-setosa","petallength"].min(), iris_data2.loc["Iris-versicolor","petallength"].min(), iris_data2.loc["Iris-virginica","petallength"].min()]
petallength_mean =[iris_data2.loc["Iris-setosa","petallength"].mean(), iris_data2.loc["Iris-versicolor","petallength"].mean(), iris_data2.loc["Iris-virginica","petallength"].mean()]
petallength_max = [iris_data2.loc["Iris-setosa","petallength"].max(), iris_data2.loc["Iris-versicolor","petallength"].max(), iris_data2.loc["Iris-virginica","petallength"].max()]

petalwidth_min = [iris_data2.loc["Iris-setosa","petalwidth"].min(), iris_data2.loc["Iris-versicolor","petalwidth"].min(), iris_data2.loc["Iris-virginica","petalwidth"].min()]
petalwidth_mean = [iris_data2.loc["Iris-setosa","petalwidth"].mean(), iris_data2.loc["Iris-versicolor","petalwidth"].mean(), iris_data2.loc["Iris-virginica","petalwidth"].mean()]
petalwidth_max = [iris_data2.loc["Iris-setosa","petalwidth"].max(), iris_data2.loc["Iris-versicolor","petalwidth"].max(), iris_data2.loc["Iris-virginica","petalwidth"].max()]

a=np.array([sepallength_min, sepallength_mean, sepallength_max, sepalwidth_min, sepalwidth_mean, sepalwidth_max])
df=pd.DataFrame(a, columns=['Iris-setosa','Iris-versicolor ','Iris-virginica'], index=['sepallength_min','sepallength_mean','sepallength_max', 'sepalwidth_min', 'sepalwidth_mean', 'sepalwidth_max'])

df.plot(kind='bar', rot= 0, figsize= (10,5)) 
plt.gcf().canvas.set_window_title('sepal comparsions')
plt.show()


b=np.array([petallength_min, petallength_mean, petallength_max, petalwidth_min, petalwidth_mean, petalwidth_max])
df=pd.DataFrame(b, columns=['Iris-setosa','Iris-versicolor ','Iris-virginica'], index=['petallength_min','petallength_mean','petallength_max', 'petalwidth_min', 'petalwidth_mean', 'petalwidth_max'])
df.plot(kind='bar', rot= 0, figsize= (10,5)) 
plt.gcf().canvas.set_window_title('petal comparsions')
plt.show()


'''
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