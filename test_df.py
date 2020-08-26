import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_csv('asdf.csv')
print(df.shape)
# print(df)
df = df[df['market_cap_rank'].notna()]
print(df.shape)