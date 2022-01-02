# Michelle Sun
# 01012022
# Watch time statistics

import pandas as pd
import ast
import datetime
import plotly.express as px

data = pd.read_csv('data/tiktok_data.csv')
times = data["timeWatched"]
time_watched = 0
month_time = 0
time_per_month = {}
year = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
        7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
tpm = []

for i in range(len(times) - 1):
    date1, date2 = times[i].split(" "), times[i + 1].split(" ")
    d1, d2 = [int(i) for i in date1[0].split("/")], [int(i)
                                                     for i in date2[0].split("/")]
    t1, t2 = [int(i) for i in date1[1].split(":")], [int(i)
                                                     for i in date2[1].split(":")]

    dt1, dt2 = datetime.datetime(d1[2], d1[0], d1[1], t1[0], t1[1]), datetime.datetime(
        d2[2], d2[0], d2[1], t2[0], t2[1])

    time_delta = dt1 - dt2
    total_seconds = time_delta.total_seconds()

    if total_seconds < 360:
        time_watched += total_seconds
        month_time += total_seconds
        time_per_month[year[d2[0]]] = month_time / 60

        if d1[0] != d2[0]:
            d1_delta = (t1[0] * 360) + (t1[1] * 60)
            month_time -= d1_delta
            time_per_month[year[d2[0]]] = month_time / 60
            month_time = d1_delta

    if d1[0] != d2[0]:
        time_per_month[year[d2[0]]] = month_time / 60
        month_time = 0

for t in time_per_month.keys():
    tpm.insert(0, [t, time_per_month[t]])

df = pd.DataFrame(tpm, columns=["Month", "Minutes Watched"])

fig = px.bar(df, x="Month", y="Minutes Watched")
fig.show()
print(tpm)
