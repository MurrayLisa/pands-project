import pandas as pd
iris_data = pd.read_csv('data.csv')
iris_data2 = iris_data.set_index("class", drop = False)
print (iris_data2.loc["Iris-setosa","sepallength"].min())


