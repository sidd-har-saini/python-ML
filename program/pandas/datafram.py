"""
pandas dataframe is two dimension like structure ,to store data in tabular form
make it easier to organize and analysis the data ,
it can store different tyoe of data list , dict , array , and other external file 
csv , excle 

creating datafram from dict 
here keys represent column 
and values represent rows

the index of list need to be equal otherwise it raise valueerror 
"""
import pandas as pd
dict = {
    'name':['siddharth','sohal','mohan'],
    'age':[20,19,20]
}
df = pd.DataFrame(dict)
print(df)

"""
working with rows and column 
we can perform basic task such as 
- adding 
- removing 
- renamin 
- selecting 

column selection
we can select specific column using columns = ['col_name']
if column not in data then it creat one and return null values 
we can also do it like (df[['name',;'age']])
"""
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

df = pd.DataFrame(data,columns=['Name','Age'])
print(df)
print(df[['Name']])
"""
Pandas provide unique methods for selecting rows from a Data frame.
 DataFrame.loc[] method is used for label-based selection
 *** label based :otherwise raise keyerror 
 """
df = pd.read_csv('student.csv', index_col= 'name')
d = df.loc['John Deo']
print(d)
df = pd.read_csv('nba.csv',index_col = 'Name')
d = df.loc['Avery Bradley']
print(d)


"""
indexing 
1: indexing using indexing operator[] this operator allow  us to fetch data from one or more columns
"""
df = pd.read_csv('student.csv',index_col='name')
da = df[['mark','gender']]
print(da)
"""
we can also use .loc[] and .iloc[] functions for indexing it give data from particluar row  it , 
this method used to select data by label
.loc[] is versatile because it can select both rows and columns simultaneously based on labels.
"""
data = df.loc['John Deo']
print(data)

"""
indexing using indexing operator and label row 
"""
df = pd.read_csv('student.csv' , index_col = 'name')
da = df['gender']
print(da)
print(df)
data = df[['mark','gender']]
print(data)
"""
indexing in dataset using .iloc[]
using .iloc[] we can chose select data row using integer unlike .loc[] which required label name 
"""
df = pd.read_csv('student.csv', index_col='name')
data = df.iloc[1]
print(data)
"""we can only pass single index not multiple otherwise it raise indexingerror,
if we want more then one row we need to pass list inside the parameter """

data = df.iloc[[1,2]]
print(data)
data = df.iloc[[1,2,3,4]]
print(data)
print(df.iloc[[1]])
for i in range(10):
    print(df.iloc[[i]])
"""
head() function return the first given values acc to pass parameter 
head(5) it return the first 5 column from the dataset
"""
print(df.head(5))
print(df.head(10))
"""
we can also use head() function to return particular column 
"""
col = df['mark']
print(col.head(5))
col = df['class']
print(col.head(5))
"""
selecting multiple columns"""
collst = df[['class','mark','gender']]
print(collst.head(5))
print(collst.head(10))

"""
selecting specific row and column using .loc[] 
.loc[['row'],['colum1','column2']]
"""
df = pd.read_csv('student.csv' , index_col='name')
data = df.loc[['John Deo','John Mike'],['id','mark','gender']]
print(data)
data = df.loc[:,['id','mark']]
print(data)
"""
':' symbol means select all 
"""
"""
indexing using .iloc[] 
.iloc[[specific row],[specific col]]
.loc[:,[specific col]]   all row specific columns 
.iloc[] specific row and its columns 
"""
print(df.loc[:,['mark','gender']])
print(df.iloc[[1,2],[1,2]])
print(df.iloc[5])
data = df.iloc[:,[1,2]]
print(data)
"""
other use full indexing method 
- head()
- tail() : return the n last value from dataset 
- at[] select specific rows's specific columns
"""
data = df.at['Alex John', 'mark']
print(data)
"""
.query() : query the datafram using boolean expression 
"""
data  = df.query("mark<75 and gender == 'female'")
print(data)
data = df.query("mark > 75 and gender == 'male'")
print(data)
data = df.query("name == 'Max Ruin'")
print(data)
print(df.query("id>10 and mark <75 and gender == 'female'"))

"""
other functions
.iat[] = it take integer values instade of label row
"""
df = pd.read_csv('student.csv' , index_col = 'name')
col_index = 2 #marks
row_index = 2 
print(df.iat[row_index,col_index])

"""
.pop() function 
The pop() method in Pandas is used to remove a column from a DataFrame and return it as a Series. 
This is similar in concept to the dictionary pop() method in Python, but specifically designed for use with Pandas DataFrames.
 It's key features include:

-Removes a specified column from a DataFrame.
-Returns the removed column as a Pandas Series.
-Modifies the original DataFrame in-place.
"""
df = pd.read_csv('student.csv')
data = df.pop('dob')
print(data) # it return the deleted column in serice 
print(df)  # it return the updated datafram (datafram get updated in place)

"""
Pandas Series.xs() function return a cross-section from the Series/DataFrame for the given key value.
"""
df = pd.read_csv('student.csv' , index_col = 'name')
data = df.xs(key = 'John Deo')
print(df)
print(data)
data = df.xs(key = 'Gain Toe')
print(data)
"""
output id                 1
class           Four
mark              75
gender        female
dob       26-11-2010
Name: John Deo, dtype: object
id                34
class          Seven
mark              69
gender          male
dob       26-11-2010
Name: Gain Toe, dtype: object
"""

"""
get() method return the particulare column from the data set
"""
df = pd.read_csv('student.csv' , index_col='id')
data = df.get(['name','mark','gender'])
print(data)

"""
datafram.isin() funtion is powerfull tool for filtering and selecting\ data from dataset it filter data set based on specific condition
type of isin()
single parameter filter 
multiple parameter filter
"""
df = pd.read_csv('student.csv' )
data = df.query("gender == 'female' and mark > 75")
print(data)

"""
.where()
this function allow you to replace values where condition is false , with certain values 
default is NaN 
"""
data = {
    'a' : [1,2,-1],
    'b' : [-1,-1,3]
}
df = pd.DataFrame(data)
#print(data)
print(df.where(df>0))
print(df.where(df<0))
"""
df.where(condition , other = 0)
other = 0  it replace that value with given valye
"""
print(df.where(df<0 , other = 0))
print(df.where(df>0 , other = 0))
df = pd.read_csv('student.csv')
print(df.where(df['id']>10 , other = 0))
print(df.where(df['mark']<75,other = 'false'))
print(df.where(df['gender']=='female',other = 0))
"""
df.where(condition , inplace = true) applied changes directly df 
"""
"""
df.insert(position,column label,values,allow_duplicates= 'False'/True)
insert func is used to insert column into dataset at particular column with name and given values 
"""
data ={
    'a':[1,2,3],
    'b':[4,5,6]
}
df = pd.DataFrame(data)
print(df)
df.insert(2,'c',3)
print(df)
"""
output
   a  b  c
0  1  4  3
1  2  5  3
2  3  6  3
"""
df.insert(1,'a',[1,2,3],allow_duplicates= True) # it by default false so if we try to insert duplicate then it threo valueError 
print(df)
s = pd.Series([100,200,300] , index=[0,1,2])
df.insert(1,'s',s)
print(df)