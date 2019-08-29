import chart_studio.plotly as py
import cufflinks as cf
import pandas as pd
import numpy as np


#fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
#fig.write_html('first_figure.html', auto_open=True)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/widgets/master/ipython-examples/311_150k.csv', parse_dates=True, index_col=1)
df.head(3)

series = df['Complaint Type'].value_counts()[:20]
series.head(3)



series.iplot(kind='bar', yTitle='Number of Complaints', title='NYC 311 Complaints',
             filename='cufflinks/categorical-bar-chart')

