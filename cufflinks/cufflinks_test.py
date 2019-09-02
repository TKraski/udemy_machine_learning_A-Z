import chart_studio.plotly as py
import plotly
import cufflinks as cf
import pandas as pd
import numpy as np
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
cf.go_offline()

# Offline html saving
df = pd.DataFrame(np.random.randn(1000, 3), columns=['A', 'B', 'C']).cumsum()
fig = df.iplot(asFigure=True)
plotly.offline.plot(fig, filename="cufflinks/example.html")
