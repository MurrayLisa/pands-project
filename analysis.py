
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
print ('Number of Rows and Colums in data set:', iris_data.shape, '\n')

# Analyses the Iris data set by class and size and prints out the number of data available per class/species
iris_data['class'].unique()
print (iris_data.groupby('class').size(), '\n')
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

#Plotting Andrews plot
# importing the andrew curve from pandas
from pandas.plotting import andrews_curves
andrews_curves(iris_data, 'class')
plt.gcf().canvas.set_window_title('Andrews Plot of the Iris Species')
plt.title('Andrews Plot of all Iris Data')
plt.show()

# importing scikit-learn, a tool used in machine learning for data mining and data analysis;
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.metrics import accuracy_score
import numpy as np

# with scikit learn (sklearn) there can be forced future warnings that do not impact the output of the code, here the warning outputs are being 'turned off'
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn


# Split-out validation dataset, first defining the array
array = iris_data.values
# defining the size of the axis
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.15
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# Test options and evaluation metric, a seed is an initial number used as the starting point in a random number generating algorithm
seed = 7
scoring = 'accuracy'


# Checking the Algorithms for Logistic Regression (LR), Linear Discriminant Analysis (LDA), K-Nearest Neighbors (KNN), 
# Classification and Regression Trees (CART), Gaussian Naive Bayes (NB) and Support Vector Machines (SVM).
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))

# Using a for loop each model is being evaluated in turn
results = []
names = []
print('Mean and Standard Deviation of the Various Algorthims: ')
for name, model in models:
    #This will split our dataset into 10 parts, train on 9 and test on 1 and repeat for all combinations of train-test splits
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)
    
#printing out blank lines to make data more presentable    
print ("")

# Compare Algorithims for accuracy and printing a box plot with the results
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.gcf().canvas.set_window_title('Comparsion of accuracy of the Algorithims')
plt.show()

# Make predictions on validation dataset
svm = SVC()
svm.fit(X_train, Y_train)
predictions = svm.predict(X_validation)
print('Accurarcy score: ', accuracy_score(Y_validation, predictions),'\n')

# Confusion matrix to evaluate the quality of the output of a classifier on the iris data set. 
print('Confusion Matrix: ')
print(confusion_matrix(Y_validation, predictions))

#Classification report of the accurracy of the SVM Algorithim
print("")
print('Classification Report: ')
print(classification_report(Y_validation, predictions))

#Defining the user input required
sepalWidth = input("Please enter Sepal width (cm): ")
sepalLength = input("Please enter Sepal length (cm): ")
petalWidth = input("Please enter Petal width (cm): ")
petalLength = input("Please enter Petal length (cm): ")
print ()

# Assigning the variables inputted by user into an array
flowerArray = [sepalWidth, sepalLength, petalWidth, petalLength]

#Loading the data set
iris = load_iris()
x = iris.data # storing feature matrix in "X"
y = iris.target # storing response vector in "y"

# fitting the data set
svm.fit(x, y)
#Predicting the species
result = svm.predict([flowerArray])

#defining the output 
print("This is most likely the ", iris.target_names[result], "species.")
