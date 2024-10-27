# for series 
import pandas as pd;

# n1 = pd.Series([1,2,3,4,5])
# print(n1)

# changing index
# n1 = pd.Series([1,23,4,5,6],index=['a','b','c','d','e'])
# print(n1)

# series from deictionary
# n = pd.Series({'k1':10, 'k2':20, 'k3':30})
# print(n)

# changing Index
# n = pd.Series({'a':10, 'b':20, 'c':30} , index=['b','c','r','a'])
# print(n)

# extracting values
# n = pd.Series([1,2,3,4,5,6,7])
# print(n[2])
# print(n[-3:])
# print(n[:4])

# basic math operation
n = pd.Series([1,2,3,4,5,6])
# n = n * 5
n2 = pd.Series([10,20,30,40,50,60])
print(n+n2)
