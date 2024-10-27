import numpy as np
import pandas as pd

# n = pd.DataFrame({
#     'Name':['rohan','rohit','ram'],
#     'marks':[90,99,89],
#     'rollno':[1,2,3]
# })



n = pd.read_csv('cardio.csv')
# first five dataset
# a = n.head()

# last 5 data set
# a = n.tail()
# print(a)

# to check how much rows and columns
# n1 = n.shape
# print(n1)

# to display all maths function mean median 
# a = n.describe()
# print(a)


# methrds
# iloc - given length of rows and data
# a = n.iloc[0:3, 6:8]
# print(a)

# loc - 
# a = n.loc[1:10,("Product","Fitness")] 
# # n.loc[[2,150],("Product","Fitness")]
# print(a)
# print(n.head())

# dropping columns
# a = n.drop("Miles",axis=1)
# print(a.head())

# dropping rows
# a = n.drop([1,2],axis=0)
# print(a.head())

# max
# print(n.max())
# min
# print(n.min())

# mean


# a  = n.loc[1:10,("Education","Age","Usage","Fitness","Income","Miles")]

# n1 = a.mean()
# print(n1)

# n2 = a.median()
# print(n2)


# panda functions #


# def double(s):
#     return s*2


# n1 = n[["Education","Age"]].apply(double)
# print(n1.head())

# more functions
# n1 = n['MaritalStatus'].value_counts()
# print(n1)

# n1 = n.sort_values(by='Age')
n1 = n.sort_values(by='Miles')
print(n1.head())