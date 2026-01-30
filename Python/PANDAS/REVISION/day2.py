# read csv file in pandas
import pandas as pd
dataFrame = pd.read_csv("filename")
print("Our DataFrame..",dataFrame)

# read excel file in pandas
import pandas as pd
df = pd.read_excel("filename")
print(df)

# we have to use specific sheet of excel 
import pandas as pd
df = pd.read_csv("filename",sheet_name = "s1")
print(df)

# if we have to use specific cols
import pandas as pd
df = pd.read_csv("filename",usecols =["col names"])
print(df)

# if we dont want to use first row then
import pandas as pd
df = pd.read_csv("filename",skiprows=1)
print(df)

# several conditions in pandas
import pandas as pd
df = pd.read_csv("filename")
print(df)
type(df)

# view first 5 rows of the table
df.head()
df.head(2)

# last 5 rows
df.tail()

# random rows
df.sample(5)

# checks total number of rows and cols
df.shape
df.size

# returns dimensions
df.ndim

# get summary
df.info()
df.describe()

# creating new columns
import pandas as pd
df = pd.read_csv("filename")
print(df)
df[['order_id','customer id',  'cuisine_type','cost_of_the_order', 'day_of_the_week', 'food_preparation_time']]
df['Order Completion time'] = df['food_preparation_time'] + df['delivery_time']
print(df)

# using filter operations in pandas
# Filter data : Students secured greater than 80 marks in Physics
df[df["Physics"]>80]

# Filter data : Students name is "Samarth"
df[df["First Name"]=="Samarth"]

# Filter records whoes First name is Arjun and Tarun using operator
df[(df["First Name"]=="Arjun") | (df["First Name"]=="Tarun")]

# Sorts the DataFrame by the specified column(s):
df.sort_values(by="Last Name")
df[df.duplicated()]

# slicing data from pandas
 # 1) loc for label-based slicing:Selecting rows and columns using labels # last index included
 # 2) iloc for positional slicing:Selecting rows and columns by integer position # last index excluded
 # 3) at for quick access to single values
 # 4) iat for quick access to single values by position
# import new table
import pandas as pd
df = pd.read_excel(r"C:\Users\Chinmay Deshpande\Desktop\Atharv Penter\Python\PANDAS\REVISION\Input data.xlsx")
print(df)
df.loc[0]
df.loc[0:4]
df.iloc[0:4]
df.iloc[0:4,[0,1,5]]
df.loc[0:3 , ["First Name","Last Name"]]
 # positional slicing:Selecting rows and columns by integer position
df.iloc[0:3,[0,1]]

 # positional slicing:Selecting rows and columns by integer position
df.iloc[0:3,[0,1]]

# iat: Accessing a single value by position
df.iat[1, 2] 

# renaming rows
df.rename(index = {0 : "Zero",1:"One",2:"Two"})
df.rename(columns = {"English" : "Eng",
                        "Physics":"Phy",
                        "Chemistry":"Chem"})

# Concatination
import pandas as pd
df = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index = [0,1,2,3]
)
df1 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7],
)
pd.concat([df,df1],axis = 0)

# Merge
# import new table
Catalog=pd.read_excel(r"C:\Users\Chinmay Deshpande\Desktop\Atharv Penter\Python\PANDAS\REVISION\Merge Input data.xlsx",sheet_name="Catalog")
Eng=pd.read_excel(r"C:\Users\Chinmay Deshpande\Desktop\Atharv Penter\Python\PANDAS\REVISION\Merge Input data.xlsx",sheet_name="Eng")
Phy=pd.read_excel(r"C:\Users\Chinmay Deshpande\Desktop\Atharv Penter\Python\PANDAS\REVISION\Merge Input data.xlsx",sheet_name="Phy")
Chem=pd.read_excel(r"C:\Users\Chinmay Deshpande\Desktop\Atharv Penter\Python\PANDAS\REVISION\Merge Input data.xlsx",sheet_name="Chem")
Math=pd.read_excel(r"C:\Users\Chinmay Deshpande\Desktop\Atharv Penter\Python\PANDAS\REVISION\Merge Input data.xlsx",sheet_name="Math")
print("Catalog", len(Catalog))
print("Eng", len(Eng))
print("Phy", len(Phy))
print("Chem", len(Chem))
print("Math", len(Math))

data = pd.merge(Catalog, Eng,       on= "Roll No" ,how="left")
print(data)
data2 = pd.merge(data, Phy,on= ["First Name","Last Name"] ,how="left")
print(data2)