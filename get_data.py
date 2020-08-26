import os
import pandas as pd

from Coingecko import Coingecko
from Sqlite import Sqlite
from Logger import logger

pd.set_option('display.max_columns', None)
from pprint import pprint as pp




abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

db_file = '../db/cg-2020.db'
sl = Sqlite(db_file)
con = sl.create_connection()
cg = Coingecko()


df = cg.coins_markets()
print(df)
# df.to_csv('asdf.csv', index=None)

df.to_sql('coins', con, if_exists='append')

