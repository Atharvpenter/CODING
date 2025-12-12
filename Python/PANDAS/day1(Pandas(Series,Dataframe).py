# Creating a series
import pandas as pd
s = pd.Series([10,20,30,40,50,60])
print(s)
s2 = pd.Series([100,200,300],index=['a','b','c'])
print(s2)

mark = {"maths":88, "science":99}
print(mark)
s3 = pd.Series(mark)

# DataFrame
# dictionary of list
data = {
    'name':['atharv','ram'],
    'age':[22,99],
    'city':['pune','sangamner']
}
df = pd.DataFrame(data)
print(df)

data1 = [
    {"name":"Akshaya","salary":2000},
    {"name":"Riya","salary":3000},
    {"name":"Karan","salary":5000}
]
df1 = pd.DataFrame(data1)
print(df1)