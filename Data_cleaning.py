#importing neccessary libraries
import pandas as pd
import numpy as np 

#Loading the dataset
df=pd.read_csv("Employee_dataset.csv")
print(df.head(10))

#checking the missing values
print("missing values in each column")
print(df.isnull().sum())

df['Salary'].fillna(df["Salary"].mean(),inplace=True)
df['Salary'] = df['Salary'].astype(int)
df['Age missing']=df["Age"].isna().astype(int)

df.replace([np.inf,-np.inf],np.nan,inplace=True)
df.fillna(df.mean(numeric_only=True),inplace=True)

#remove duplicates
df.drop_duplicates(inplace=True)

#Handling outliers
salary_mean= df["Salary"].mean()
salary_std= df["Salary"].std()
lower_bound= salary_mean - (3*salary_std)
upper_bound=salary_mean + (3*salary_std)

#Remove rows where salary is too high and too low
df= df[(df["Salary"]>=lower_bound) & (df["Salary"]<=upper_bound)]

#save cleaned data
df.to_csv("Employee_cleaned_dataset.csv",index=False)

#save as excel
df.to_excel("Employee_cleaned_dataset.xlsx",index=False)

#show last few rows
print(df.head())