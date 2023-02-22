import pandas as pd
pd.set_option("display.max.rows",None)
pd.set_option("max_colwidth",None)
#Q7
df = pd.read_csv (r'ds_salaries.csv')
change = df.groupby(["job_title","work_year"]).mean()["salary_in_usd"]
print(change)
