import pandas as pd
pd.set_option('display.max_columns', 20)
from Sqlite import Sqlite
from Logger import logger

db_file = '../db/cg-2020.db'
sl = Sqlite(db_file)
con = sl.create_connection()

# get all items from db
query = 'SELECT * from coins'
# query = 'SELECT * from coins WHERE id="bitcoin"'
df = pd.read_sql_query(query, con)
logger.info(str(df.shape[0]) + ' items queried..')


# query = 'SELECT * from coins WHERE symbol="eth"'



print(df)
con.close()