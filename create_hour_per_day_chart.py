import os
import plotly.plotly as py
from plotly.graph_objs import *

import config

py.sign_in(config.plotly_user, config.plotly_pass)

dates = []
count_dates = []
counts = []
hours = []

with open(os.path.normpath(config.filename), 'r') as f:
    rows = f.readlines()

# get summary of dates in file
    for line in rows:
        lines = line.strip().split(',')
        just_date = lines[0].split(' ')
        dates.append(just_date[0])
        bins = sorted(list(set(dates)))

# count occurrences per day
    for line in rows:
        lines = line.strip().split(',')
        just_date = lines[0].split(' ')
        if lines[1] == ' 1':
            # gaming happened
            count_dates.append(just_date[0])

# sort date events into bins
for bin in bins:
    counts.append(count_dates.count(bin))

# normalise 5 min slots into actual hours
for count in counts:
    hours.append(count/float(12))

trace1 = Bar(x=bins,y=hours)

data = Data([trace1])

layout = Layout(
    title = config.plotly_graph_title,
    xaxis=XAxis(
        title='Date',
        autorange=True
    ),
    yaxis=YAxis(
        title='Number of Hours',
        autorange=True
    )
)

fig = Figure(data=data, layout=layout)

# do the graph magic
plot_url = py.plot(fig, filename=config.plotly_url, fileopt=config.plotly_fileopt, auto_open= config.plotly_auto_open)
