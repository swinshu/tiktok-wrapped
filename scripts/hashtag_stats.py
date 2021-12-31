# Michelle Sun
# 12302021
# Filtering data for hashtag statistics
import re
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/tiktok_data.csv")

df['desc'] = df['desc'].str.ljust(1)
df = df.dropna(subset=['desc'])

hashtags = {}
tag_num = []
foryoutags = ['fyp', 'foryou', 'foryoupage', 'fy', '4u']

for d in df['desc']:
    tags = re.findall('\#(.*?)(?=\s|\#)', d)
    for t in tags:
        try:
            hashtags[t] = hashtags[t] + 1
        except:
            hashtags[t] = 1
            continue

for ht in hashtags.keys():
    if ht not in foryoutags:
        tag_num.append([ht, hashtags[ht]])

df_tags = pd.DataFrame(tag_num, columns=["Hashtag", "Number of Tiktoks"])
df_tags = df_tags.sort_values(
    by=["Number of Tiktoks"], ascending=False).head(50)

fig = px.bar(df_tags, x='Hashtag', y='Number of Tiktoks')
fig.show()
