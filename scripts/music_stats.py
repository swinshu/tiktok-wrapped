# Michelle Sun
# 12302021
# Getting and organizing watch (music) data

import pandas as pd
import matplotlib.pyplot as plt
import ast
import plotly.express as px

data = pd.read_csv('data/tiktok_data.csv')
songs = data['music']
occ = {}
lst = []
ids = {}
unique_songs = 0

for s in songs:
    try:
        dict_data = ast.literal_eval(s)
        song_name = dict_data.get('title')
        song_id = dict_data.get('id')
        # print(song_name)
    except Exception as e:
        print(e)
        continue
    try:
        occ[song_name] = occ[song_name] + 1
        ids[song_id] = ids[song_id] + 1
    except:
        occ[song_name] = 1
        ids[song_id] = 1
        continue

del occ['original sound']

unique_songs = len(ids)

# print(unique_songs)

for s in occ.keys():
    lst.append([s, occ[s]])

df = pd.DataFrame(lst, columns=["Song Title", "Number of Videos"])
df = df.sort_values("Number of Videos", ascending=False).head(50)

fig = px.bar(df, x='Song Title', y='Number of Videos')
fig.show()
