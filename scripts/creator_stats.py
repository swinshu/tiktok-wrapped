# Michelle Sun
# 12302021
# Getting and organizing watch (creator) data

import pandas as pd
import matplotlib.pyplot as plt
import ast
import plotly.express as px

data = pd.read_csv('data/tiktok_data.csv')

tiktokers = {}
creators = {}
authors = data['author']
# invalid = []
tiktokers_list = []

for d in authors:
    try:
        dict_data = ast.literal_eval(d)
        authorId = dict_data.get('uniqueId')
    except Exception as e:
        # invalid.append(d)
        print(e)
        continue
    try:
        tiktokers[authorId] = tiktokers[authorId] + 1
    except:
        tiktokers[authorId] = 1
        continue

for tik in tiktokers.keys():
    if tiktokers[tik] > 3:
        creators[tik] = tiktokers[tik]

for name in creators.keys():
    tiktokers_list.append([name, creators[name]])

df = pd.DataFrame(tiktokers_list, columns=['Creator', 'Views'])
df_out = df.sort_values(by=['Views'], ascending=False)

fig = px.bar(df_out, x='Creator', y='Views')
fig.show()
