'''
A small script to show the various methods involved in EDA
'''

import pandas as pd
import numpy as np
import matplotlib


df = pd.read_csv("survey.csv")

'''
Understanding the data:
First we print a preview(the first 5 rows of the data frame...)
'''
#print(df.head())

'''
then we print the last 5 entries
'''
#print(df.tail())

'''
shape shows how many rows and columns are there
'''
#print(df.shape)


'''
This command will show an overview/summary of the file involved, info like columns,mem usage, datatypes and the non-null values in the table
'''
#print(df.info())

'''
this prints out any duplicates in the dataframe
'''
#print(df.duplicated().sum())


'''
We can find the unique values of a certain column
'''
#print(df["City"].unique())
#print(df["Position"].unique())

'''
then to check how many values each entry has
'''
#print(df["City"].value_counts())

'''
Check for null values in the df, this checks how many null values are there in each clolumn
'''
#print(df.isnull().sum())

'''
We can then replace all null values with 0 or any value...
After replacing the values we run the check again
'''
# df.replace(np.nan, "0", inplace=True)

# print(df.isnull().sum())

#print(df.boxplot())

'''
We can get an overview/ description of the Gender(or any) column
===
One point to not is that calling describe on the whole dataframe only shows summary of the integer values.
'''
#print(df["Gender"].describe())
#print(df.describe()) #->only shows summary of integer values