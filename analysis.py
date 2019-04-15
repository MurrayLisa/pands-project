#Pandas is an open source data analysis library
import pandas as pd
iris_data = pd.read_csv("data.csv")
iris_data_colums = ["sepal_length","Sepal_width", "Petal_length", "Petal width", "Species" ]
print(iris_data)
