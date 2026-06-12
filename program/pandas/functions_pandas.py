"""
.isnull()
it check where the dataset contain null values or not 
is yess it return true (return all data if null true not null false otherwise)
.isnull().sum() 
it check and count the null value and return the total null values
"""
import pandas as pd
data = pd.read_csv('student.csv')
#n = data.isnull()
#print(n)
n2 = data.isnull().sum()
print(n2)
d = data.fillna(0)
print(data)
n = data.isnull().sum()
print(n)

"""
.fillna() function is used to replace null value with given values 
"""
"""
selecting and filtering 
this method filter and select specific column from table and retrive it based on certain conditions 
"""
data = pd.read_csv('student.csv')
d = data[(data['gender'] == 'female') & (data['mark']>89)]
print(d)
d = data.query("gender == 'female'")
print(d)
"""
threshold values 
use @ 
@ tell pandas to use python variable 
"""
mark = 70
val = data.query("mark < @mark")
print(val)

"""
noraml fiter and sorting method is same as the .query method 
the diff is syntaxx 
df[['mark'>50]] and .query("gender == 'female'")
"""
"""
adding and removing columns from dataset 
you can create new column based on existing one and delect 0ne 
"""
data = pd.read_csv('student.csv')
data['performance'] = (data['mark'] / 100)* 100
print(data) 
print(data.head())

print(data.describe())
"""
.describe() method in pandas 
tell the totel
-count 
-mean 
-std
-min
-25%
-50%
-75%
-max 
of the total values
"""
"""
removing column from datasrt 
here we can use 
----------------------------
.drop()
ex  datafram.drop('mark',axis = 1,inplace =True)
axis = 1 means column 
inplace = true mean modified into real dataset on real time 
we can also use columns =[]  method 
ex datafram.drop(columns=['mark','gender'])
----------------------------
.pop()
pop method remove column from dataset and return in serice 
-------------------------------
del 
del datafram['mark']
method remove column parmently 
aggressive one
"""

#pop()
#d = data.pop('performance')
#print(d)
#print(data)

#del method  
#del data['performance']
#print(data)

#.drop() 
#d = data.drop(['performance' ,'dob'], axis= 1 , inplace=True)
#print(d)
#print(data)
"""
print(data.axes)
print(data.index)
# this method return both row and column index label and other info
"""
"""
groupby()
is method that based on split-apply-combine concept where it spilt common column values apply funcion
and combine and return result 
"""
data = {
    'Department': ['HR', 'IT', 'IT', 'HR', 'Sales', 'Sales'],
    'Salary': [50000, 70000, 80000, 52000, 60000, 65000],
    'Bonus': [3000, 5000, 4500, 3500, 2000, 2500]
}
df = pd.DataFrame(data)
print(df)
cat = df.groupby('Department')['Salary'].std()
cat = df.groupby('Department')['Salary'].mean()
print(cat)
cat = df.groupby('Department')
print(cat.first())
cat = df.groupby('Salary')
print(cat.first())

#groupby using single parameter 
data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi',
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'],
        'Age':[27, 24, 22, 32,
               33, 36, 27, 32],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA']}
df = pd.DataFrame(data1)
grp = df.groupby('Name').groups  #.groups return the grouped data inform of dict 
# {'Abhi': [7], 'Anuj': [1, 5], 'Gaurav': [4], 'Jai': [0, 2], 'Princi': [3, 6]}
print(grp)

# groupby passing more then one parameter
df = pd.read_csv('nba.csv')
#print(df)
grp = df.groupby(['Team' , 'Salary']).agg( total_salary = ('Salary','sum'),avg = ('Salary','mean'))
print(grp)
print(df)
grp = df.groupby('Team')['College']
print(grp.first())
grp = df.groupby('College')['Team']
print(grp.first())


"""
appling aggregration funtion on groupby 
aggregration function .sum() .mean() .avg() .std() .var() .prop()
"""

df = pd.read_csv('nba.csv')
grp = df.groupby(['Team','College']).agg(total_salary =('Salary','sum'),avg = ('Salary','mean'))
print(grp)
grp = df.groupby('Team').agg(avg_age= ('Age','mean'))
print(grp)
print(grp.describe())
print(len(grp))   # 30
print(grp.size)   # 30
print(grp.ndim)   # 2 dim
print(grp.shape)  #(30,1)


"""
transformation function 
aggegration function chages the shape of the group after appling certain operation on the group
but in transfromation function is group specific function which dont change the size of the grp 
after the operation 
"""
df['grp_by_sal'] = df.groupby('Team')['Salary'].transform(lambda x: x.rank(ascending=False))
print(df)
grp = df.groupby('Team')['Height'].transform(lambda x: x.rank(ascending=False))
print(grp)
df['rk_by_weigth'] = df.groupby('Team')['Weight'].transform(lambda x: x.rank(ascending=False))
print(df)

"""
using filteration method 
"""
grp = df.groupby('Team').filter(lambda x: x['Weight'].mean()>200)
print(grp)


print(df.columns)
"""
this .columns function return the total column name 
"""
print(df.dtypes)
""" this function return the data type of the columns """

df = df.sort_values('Salary' , ascending= False)
print(df)
""" this sort_values() function used to arrange the data set in sorted form"""
df = df.sort_values('Height',ascending = True)
print(df)
gp = df.sort_values('Weight',ascending=True)
print(gp)

print(df.sort_values("Weight"))


""" pandas .unique() return the unique value from the serise """
""" here it also count NaN as unique value
and it only applicable for serise not dataframe""" 

grp = df['Team'].unique()
print(grp)
grp = df['Weight'].unique()
print(grp)
grp = df['Height'].unique()
print(grp)

"""
nunique() return the no of uniques value occue in serise 
nunique(axis,dropna=true)
"""
# importing pandas as pd
import pandas as pd

# Creating the first dataframe
df = pd.DataFrame({"A":[14, 4, 5, 4, 1],
                "B":[5, 2, 54, 3, 2],
                "C":[20, 20, 7, 3, 8],
                    "D":[14, 3, 6, 2, 6]})

# Print the dataframe
print(df.nunique(axis=0)) # axis = 0 means column wise 
print(df.nunique(axis=1 , dropna=True)) # axis = 1 means row wise 

"""
.unique()
.nunique() """

print(df.duplicated())
""" .duplicated() function check wether a row contain duplicate values or not if yes true , if no false"""
""".drop_duplicate() function remove duplicate row from the data set"""
data = {
    'a' : ['A','A','B','D'],
    'b': [1,1,2,3]
}
df = pd.DataFrame(data)
print(df.duplicated())
db = df[df.duplicated()]
print(db)
print(df.drop_duplicates())
print(df)

""".str is string accessing operator by which we can access string in dataset and 
perform operation on it """
data = {
    'name' : ['atharv','anshu','babu','gujiya','gudden'],
    'mark' :[89,98,80,85,87]
}
import pandas as pd
df = pd.DataFrame(data)
grp = df['name'].str.upper()
print(grp)
grp = df['name'].str.lower()
print(grp)
grp = df['name'].str.title()
print(grp)

""" we can also we for loop for it """
for i in df['name']:
    print(i.upper())
""" for loop just return the data """
""" but .str method return the serise of data"""
