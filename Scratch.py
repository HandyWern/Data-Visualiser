import os
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from datetime import datetime as dtm
import seaborn as sns


sns.set(font_scale=1, style="whitegrid")

Log = pd.read_csv('LOGFILE1.csv')
Time = [dtm.time(dtm.strptime(t, "%H:%M:%S")) for t in Log.Time]

##Time = [dtm.strptime(t,"%H:%M") for t in Log.Time]
##print(Time)

fig, ax = plt.subplots(figsize=(16,7))

ax.set(title="Data Visualization\nBeta")
#ax.get_xaxis().set_major_locator(ticker.MaxNLocator(nbins='auto'))
#ax.get_xaxis().set_major_formatter(ticker.IndexFormatter(Time))


plt.plot(Time,Log.Humidity, 'o')
plt.plot(Time,Log.Temperature, 'o')
plt.legend(['Humidity (%)','Temperature (C)'])
plt.xlabel('Time')
##plt.title('Data Visualization\nBeta')
plt.gcf().autofmt_xdate()

plt.show()