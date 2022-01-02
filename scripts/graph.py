# Michelle Sun
# 12302021
# Filtering data for hashtag statistics
import re
from sklearn.decomposition import TruncatedSVD
import pandas as pd
import plotly.express as px
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("data/tiktok_data.csv")

df['desc'] = df['desc'].str.ljust(1)
df = df.dropna(subset=['desc'])

hashtags = {}
tag_num = []
tag_list = []
foryoutags = ['fyp', 'foryou', 'foryoupage', 'fy', '4u']

for d in df['desc']:
    tags = re.findall('\#(.*?)(?=\s|\#)', d)
    for banned_tag in foryoutags:
        if banned_tag in tags:
            tags.remove(banned_tag)

    for t in tags:
        try:
            hashtags[t] = hashtags[t] + 1
        except:
            hashtags[t] = 1
            continue

    tag_list.append(' '.join(tags))

for ht in hashtags.keys():
    if ht not in foryoutags:
        tag_num.append([ht, hashtags[ht]])

df_tags = pd.DataFrame(tag_num, columns=["Hashtag", "Number of Tiktoks"])
df_tags = df_tags.sort_values(
    by=["Number of Tiktoks"], ascending=False)

fig = px.bar(df_tags, x='Hashtag', y='Number of Tiktoks')
# fig.show()


# count vectorizer co-occurence matrix
# making the N x K matrix
count_model = CountVectorizer(ngram_range=(1, 1), max_features=100)
X = count_model.fit_transform(tag_list)

# making the K x K matrix
Xc = (X.T * X)
Xc.setdiag(0)
Xc = Xc.todense()


# # getting vocab for graph labels
vocab = count_model.vocabulary_
vocab = {value: key for (key, value) in vocab.items()}

# making the K x 2
clf = PCA(2)
Xpca = clf.fit_transform(Xc)

# graphing
df = pd.DataFrame(Xpca)
print(df.columns)
df['label'] = [vocab[i] for i in range(len(vocab))]
fig = px.scatter(df, x=0, y=1, text='label')
fig.show()
