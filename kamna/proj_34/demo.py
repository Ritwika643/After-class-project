import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import kagglehub
from kagglehub import KaggleDatasetAdapter
import os

path = kagglehub.dataset_download("niranjandasmm/irisnumericdatasetcsv")

files = os.listdir(path)
print("Files:", files)

file_path = [f for f in files if f.endswith(".csv")][0]

iris = kagglehub.dataset_load(
  KaggleDatasetAdapter.PANDAS,
  "niranjandasmm/irisnumericdatasetcsv",
  file_path
)

column_names = ['sepal_length_cm', 'sepal_width_cm', 'petal_length_cm', 'petal_width_cm', 'species']
iris.columns = column_names

print(iris.head())
print(iris.info())
print(iris.columns)

sns.barplot(x='species', y='sepal_length_cm', data=iris)
plt.show()

sns.countplot(x='species', data= iris)
plt.show()

sns.boxplot(x='species',  y='sepal_length_cm',data=iris)
plt.show()

sns.swarmplot(x='species', y='sepal_length_cm', data=iris)
plt.show()

sns.histplot(y='sepal_length_cm', data= iris)
plt.show()

sns.jointplot( y='sepal_length_cm',data= iris)
plt.show()

sns.pairplot(data = iris, hue= 'species')
plt.show()