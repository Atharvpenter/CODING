import pandas as pd
data = {
    "Name":["atharv"],
    "age":["penter"]
}
df = pd.DataFrame(data)
print(df)

data1 = [
    {"Name":"Atharv","Age":22,"Salary":15000},
    {"Name":"ram","Age":27,"Salary":18000},
    {"Name":"Sham","Age":25,"Salary":14000}
]
df1 = pd.DataFrame(data1)
print(df1)

import numpy as np
arr = np.array([
    [1,'kunal',23],
        [2,'kshitij',24],
            [3,'akhil',23]
])
df3 = pd.DataFrame(data = arr, columns=["id","name","age"])
print(df3)

df4 = pd.read_csv('employees.csv')
print(df4)
