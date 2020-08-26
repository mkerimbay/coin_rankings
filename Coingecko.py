import requests
from pprint import pprint
import pandas as pd
base = 'https://api.coingecko.com/api/v3'
from Logger import logger


class Coingecko:

    def ping(self):
        url = "/ping"
        res = requests.get(base+url)
        if res.status_code == 200:
            return True
        return False

    def coins_list(self):
        url = "/coins/list"
        res = requests.get(base+url)
        if res.status_code == 200:
            pprint(res.headers)

    def coins_markets(self):
        url = '/coins/markets'
        i = 1
        df = None

        while True:
            params = {'vs_currency': 'usd',
                      'per_page': 250,
                      'page': i}
            res = requests.get(base + url, params=params)
            if len(res.json()) > 0:
                df = pd.concat([df, pd.DataFrame(res.json())])
                i += 1
            else:
                break

        df = df[['ath', 'ath_change_percentage', 'ath_date', 'atl',
       'atl_change_percentage', 'atl_date','current_price', 'high_24h', 'id',
        'low_24h', 'market_cap', 'market_cap_change_24h',
       'market_cap_change_percentage_24h', 'market_cap_rank',
       'name', 'symbol']]
        df = df[df['market_cap']>0]
        df = df.set_index('id')
        # print(df.shape)
        # print(df.columns)
        # print(df.head())
        logger.info(str(df.shape) + ' items fetched')
        return df



# cg = Coingecko()
# cg.coins_markets()