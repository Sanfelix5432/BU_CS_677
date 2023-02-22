import pandas as pd

s = pd.read_csv('ds_salaries.csv')

s.head()

a = s.groupby(['job_title','work_year'],as_index=False)['salary_in_usd'].mean()
df = pd.DataFrame(a)
b = df.groupby(['job_title'],as_index=False)['salary_in_usd'].max()
c = df.groupby(['job_title'],as_index=False)['salary_in_usd'].min()
df1 = pd.DataFrame(b)
df2 = pd.DataFrame(c)
df3 = df2.copy()
df3['difference'] = df1['salary_in_usd'] - df3['salary_in_usd']
df3 = df3[df3['difference'] > 0]
n1 = df3['job_title'][df3['difference']==df3['difference'].max()]
n2 = df3['job_title'][df3['difference']==df3['difference'].min()]
print(n1)
print(n2)
