# Johnny Ma
# 12-29-21
# Reading the Video History Text and outputting Date+TikTok Link rows

import pandas as pd

with open('data/Video Browsing History.txt') as f:
    lines = f.readlines()
    lines.remove('\n')

# remove random '\n'
txt = [x.replace('\n', '') for x in lines if x != '\n']

# fill two lists of dates and video links
dates = []
vids = []
for i in range(int(len(txt)/2)):
    dates.append(txt[i*2].replace('Date: ', ''))
    vids.append(txt[i*2-1].replace('Video Link: ', ''))

# output as dataframe
d = {'date': dates, 'links': vids}
df = pd.DataFrame(d)
df.to_csv('tt.csv')
