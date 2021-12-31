# Johnny Ma
# 12-29-21
# Querying the TikTok API for videos

from TikTokApi import TikTokApi
import pandas as pd
import time
from tqdm import tqdm

api = TikTokApi.get_instance()

# read in tik tok data
df = pd.read_csv('data/tt.csv')

df_out = pd.DataFrame()
invalids = []
for ind, row in tqdm(df.iterrows(), total=df.shape[0]):
    tiktok_id = row['links'].replace(
        'https://www.tiktokv.com/share/video/', '')[:-1]
    time.sleep(1)
    # to avoid invalid tiktok links
    try:
        d = api.get_tiktok_by_id(tiktok_id).get('itemInfo')
    except:
        print('invalid TikTok')
        invalids.append(tiktok_id)
        continue

    # formatting data
    df_row = pd.DataFrame.from_dict(d).T
    df_row.index = [row['date']]

    # appending to total dataframe
    df_out = df_out.append(df_row)

    # output
    df_out.to_csv('tiktok_data.csv')
