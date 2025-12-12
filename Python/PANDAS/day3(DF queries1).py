import pandas as pd
data = {
    "Name":["atharv","Ram","Sham","Tom","Jerry"],
    "Age":[22,26,23,24,18],
    "Department":["IT","CA","Finance","HR","telecalling"],
    "Salary":[35000,30000,25000,15000,18000]
}
df = pd.DataFrame(data)
print(df)
print(df[["Salary"]])
print(df[["Name"]])

# print salary above 20000
print(df[df["Salary"] > 20000])
# return boolean values
print(df["Salary"] > 20000)

# print Employee ID
print(df[df["Department"] == "IT"])

# print IT or CA department whose salary is more than 26000
print = (df['Department'] == "IT") | (df['Department'] == "HR")

