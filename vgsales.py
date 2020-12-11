import pandas as pd
df = pd.read_csv('./vgsales.csv')
df.head()
print(df.head)
df.groupby(["Year"])["Global_Sales"].mean()
df_Before2005 = df[df["Year"]<2005]
df_After2005 = df[df["Year"]>2005]
df.loc[(df["Year"]>2005),"Record"] = "Post-2005"
df.loc[(df["Year"]<2005),"Record"] = "Pre-2005"
print(df[["Name", "Year","Global_Sales" ,"Record"]])
print(df.groupby(["Record"])['Global_Sales'].mean())
