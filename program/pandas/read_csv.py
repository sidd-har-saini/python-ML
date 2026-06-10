"""
pandas : python provide opensource libary for data manupliation cleaning , analysis and work with tablular data 
flexibly and efficiently 
"""
"""
what pandas do :
data handling : handle missing value 
data cleaning : remove duplicae and fix inconsitencey 
data visulization : represent data graphically 
data transformation : filter sort , modify data 
"""
"""
data structure in pandas
pandas provide two type of data structure 
1 pandas serice is one dimension array capable of holding data of anytype 
"""
import pandas as p
import numpy as n
arr1 = n.array([1,2,3,4])
arr = p.Series(arr1)
print(arr)

"""
2 pandas dataframe is two dimension array which store data in tabular form 
"""
arr1 = n.array(["hello","world"])
arr = p.DataFrame(arr1)
print(arr)
"""
operation in pandas :
1 : read specific column using usecols , which reduce processing time and memory by processing only required 
column """

df = p.read_csv('student.csv')
print(df)
df = p.read_csv('student.csv',usecols=['name','gender'])
print(df)

"""
2 : Setting an Index Column (index_col)
The index_col parameter sets one or more columns as the DataFrame index, 
making the specified column(s) act as row labels for easier data referencing.
"""
df = p.read_csv('student.csv',index_col='name')
print(df)
#now name act as row label for easyer data referencing\
"""
3: handling missing value 
in read_csv we can use na_values which relace missing or null value with specific values
"""
df = p.read_csv('student.csv',na_values=['0','null'])
print(df)

"""
4: reading csv with different delimiter , 
"""

data = data = """totalbill_tip, sex:smoker, day_time, size
16.99, 1.01:Female|No, Sun, Dinner, 2
10.34, 1.66, Male, No|Sun:Dinner, 3
21.01:3.5_Male, No:Sun, Dinner, 3
23.68, 3.31, Male|No, Sun_Dinner, 2
24.59:3.61, Female_No, Sun, Dinner, 4
25.29, 4.71|Male, No:Sun, Dinner, 4"""

with open('sample.csv','w') as file:
    file.write(data)
print(data)
df = p.read_csv('sample.csv', sep = '[,:_|]',engine = 'python')
print(df)

df = p.read_csv('sample.csv' , sep = '[:,_|]' , engine = 'python',na_values=['0','null'])
print(df)

"""
5 : nrows , it return the certain no of row rather then returning entire table 
"""
df = p.read_csv('student.csv',nrows = 4)
print(df)
"""
6 : skiprows this function skip he specific row and return the rest data 
"""
df = p.read_csv('student.csv',skiprows=[7,4,2,6])
print(df)

"""
7 : parse_dates : The parse_dates parameter converts date columns into datetime objects
"""
print(df.info())
df = p.read_csv('student.csv',parse_dates=['class'])
print(df.info())

"""
loading csv file form link 
"""
url = "https://media.geeksforgeeks.org/wp-content/uploads/20241121154629307916/people_data.csv"
df = p.read_csv(url)
print(df)



import pandas as pd
data = pd.read_csv('student.csv', usecols = ['name' , 'gender'])
print(data)
data = pd.read_csv('student.csv' , index_col = ['name'])
print(data)
data = pd.read_csv('student.csv' , na_values = [0])
print(data)
data = pd.read_csv('student.csv', sep='[.,|_]',engine='python')
print(data)
data = pd.read_csv('student.csv', nrows = 3)
print(data)
data = pd.read_csv('student.csv', skiprows = [1,2,3,4])
print(data)
data = pd.read_csv('student.csv' , parse_dates = ['dob'] )
print(data.info())