# Fisher's Iris data Set
### By Lisa Murray

## Problem Statement

Research the Fisher's Iris data set and document the outcome in Python code.


## Background
The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: 

1. Sepal Length (cm)
2. Sepal Width (cm)
3. Petal Length (cm)
4. Petal Width (cm)


The Liner discriminant was developed to distinguish species from each other. This data set is now the typical test case for many statistical classification techniques.

The use of this data set in cluster analysis however is not common, since the data set only contains two clusters with rather obvious separation. One of the clusters contains Iris setosa, while the other cluster contains both Iris virginica and Iris versicolor and is not separable without the species information Fisher used. 



The sepals are the lower, or outermost part of the flower, they are usually green in color however  in the case of the Iris flowers they are Purple, similar in colour to the petal. 
As per the images below.


![image](https://user-images.githubusercontent.com/47781978/55834337-94c4ae00-5b11-11e9-913d-b34b0501a92c.png)

## How to download Repository and run the code

Go to Github and click on pands-project
Click Clone or download
Ensure file type is HTTPS and click Download Zip
Extract file and save in desired location

## Libraries Used
Pandas is an BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. (import pandas as pd) 

Dataframe is a 2-dimensional labeled data structure with columns of potentially different types. (from pandas import Dataframe)

NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays (import numpy as np)

Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics (import seaborn as sns)

Matplotlib.pyplot s a state-based interface to matplotlib. It provides a MATLAB-like way of plotting. pyplot is mainly intended for interactive plots and simple cases of programmatic plot generation (import matplotlib.pyplot as plt).


##Data review and Findings
The Iris data was initially downloaded from https://datahub.io/machine-learning/iris#resource-iris as a data.csv file.  CSV (comma-separated values) is a simple file format used to store tabular data, such as a spreadsheet or database.
iris_data = pd.read_csv(‘data.csv’)
All of the data was then summarised to show the count, mean, standard deviation, min and max of all class/species of the iris data set. However this analysis does not distinguish between the flowers. 
 
  ![image](https://user-images.githubusercontent.com/47781978/56591376-892cb900-65e0-11e9-9cb3-38e786f313b8.png)


 Therefore the min, mean and max was calculated for each iris data set, that is the sepal length, sepal width, petal length and petal width for each of the three classes/species of the Iris flowers (Iris setosa, Iris virginica and Iris versicolor). 

![image](https://user-images.githubusercontent.com/47781978/56589257-c5f6b100-65dc-11e9-9fff-f8035777e1d0.png)

Two bar graphs are then plotted one for sepal comparisons and one for petal comparisons:

![image](https://user-images.githubusercontent.com/47781978/56589366-fb9b9a00-65dc-11e9-9908-47c4ca3588b1.png)

![image](https://user-images.githubusercontent.com/47781978/56589435-21c13a00-65dd-11e9-9e38-17bfaabe7f60.png)

From these two graphs it is clear that there are bigger variations between all of the species in the petal comparisons, the  Iris setosa is more distinguishable that the Iris virginica and Iris versicolor.
Boxplot graphs were then used to compare the distribution of  sepal length, sepal width, petal length, petal width.

![image](https://user-images.githubusercontent.com/47781978/56589501-474e4380-65dd-11e9-8e3c-bcacc864095d.png)
![image](https://user-images.githubusercontent.com/47781978/56589563-6947c600-65dd-11e9-8cea-8b11e273dc41.png)
![image](https://user-images.githubusercontent.com/47781978/56589636-8bd9df00-65dd-11e9-8b74-85af1acca752.png)
![image](https://user-images.githubusercontent.com/47781978/56589719-b461d900-65dd-11e9-9fc4-093e381e6511.png)

From the Boxplot, we can see that there are distinct differences between the sepal length, petal length and  petal width and across the species. The sepal width has a cross over between then Iris virginica and Iris versicolor

Similar to the bar chart the a violin plot shows there are bigger variations between all of the species in the petal comparisons, the  Iris setosa is more distinguishable that the Iris virginica and Iris versicolor. The violin plot was  used to display the distribution of the data and its probability density. The thick black bar in the center represents the interquartile range, the thin black line extended from it represents the 95% confidence intervals, and the white dot is the mean.

![image](https://user-images.githubusercontent.com/47781978/56589801-d9564c00-65dd-11e9-8d66-e4f7f9093042.png)
![image](https://user-images.githubusercontent.com/47781978/56589877-fa1ea180-65dd-11e9-94da-83126f81f8e9.png)
![image](https://user-images.githubusercontent.com/47781978/56589949-18849d00-65de-11e9-8688-59fe9e2a560b.png)
![image](https://user-images.githubusercontent.com/47781978/56590040-41a52d80-65de-11e9-82bf-92ef84299452.png)


The swarm plot shows non-overlapping distribution of the attributes of the Iris species. This graph similar to above showed the petal length and width is the more distinguishing feature.  

![image](https://user-images.githubusercontent.com/47781978/56590288-c1cb9300-65de-11e9-9c7e-69c4bf3fbba7.png)

Pairs Plots builds on two basic figures, the histogram and the scatter plot. The histogram on the diagonal allows us to see the distribution of a single variable while the scatter plots on the upper and lower triangles show the relationship (or lack thereof) between two variables. The pair plot in the case of the Iris species makes a clear case of how the iris-setosa is more unique than the iris-versicolor and the iris-virginica. However it can also be clearly seen that the iris-virginica is the larger flower by having a longer sepal and petal.

![image](https://user-images.githubusercontent.com/47781978/56599780-2ee72480-65ef-11e9-9792-0e44599bb0b9.png)


## References
1. https://en.wikipedia.org/wiki/Iris_flower_data_set
2. https://www.quora.com/What-is-the-difference-between-sepals-and-petals
3. https://datahub.io/machine-learning/iris#resource-iris
4. https://seaborn.pydata.org/generated/seaborn.swarmplot.html
5. https://stackoverflow.com/questions/22408237/named-colors-in-matplotlib5. 
6. https://www.w3resource.com/graphics/matplotlib/barchart/matplotlib-barchart-exercise-11.php
7. https://matplotlib.org/gallery/lines_bars_and_markers/barchart.html
8. https://seaborn.pydata.org/generated/seaborn.violinplot.html
9. https://seaborn.pydata.org/generated/seaborn.pairplot.html
