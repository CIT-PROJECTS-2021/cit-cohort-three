import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), columns=['col1', 'col2', 'col3'])
df.apply(lambda x: x.max() - x.min())

# What method can be used to get the number of non-NA values in a pandas dataframe?
# Answer: df.count()

"""
Download a csv file from https://stats.govt.nz/assets/Uploads/Business-employment-data/Business-employment-data-June-2022-quarter/Download-data/business-employment-data-june-2022-quarter-csv.zip and load it into a pandas dataframe. How many rows and columns are there?
"""

import requests
import zipfile
import io

url = 'https://stats.govt.nz/assets/Uploads/Business-employment-data/Business-employment-data-June-2022-quarter/Download-data/business-employment-data-june-2022-quarter-csv.zip'
r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

df = pd.read_csv('machine-readable-business-employment-data-june-2022-quarter.csv')
print(df.shape)


"""
Create a dataframe with 10 rows and 3 columns, 
where the values are random numbers between 1 and 10 (inclusive). 
Then, replace all values greater than 5 with the value 10.
"""

df = pd.DataFrame(np.random.randint(1, 11, size=(10, 3)))
print("Before replacing values:")
print(df)
df[df > 5] = 10
print("After replacing values:")
print(df)

# list = [i for i in range(1, 11)]
# df = pd.DataFrame(np.random.choice(list, size=(10, 3)))



"""
create a dataframe from this link https://jsonplaceholder.typicode.com/albums
"""

# df = pd.read_json('https://jsonplaceholder.typicode.com/albums')
# df.head()
