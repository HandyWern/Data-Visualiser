import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

plt.style.use('seaborn')

data = pd.read_csv('week14.CSV')

data['Date'] = pd.to_datetime(data['Date'], format='%Y/%m/%d %H:%M:%S')

date = data['Date']
humidity = data['Humidity']
temperature = data['Temperature']

##calculate mean values
humidity_mean = [np.mean(humidity)]*len(humidity)
temperature_mean = [np.mean(temperature)]*len(temperature)

##formatting mean strings
temperature_mean_str = format(np.mean(temperature), '.2f')
humidity_mean_str = format(np.mean(humidity), '.2f')


##plot lines
temperature_line = plt.plot_date(date, humidity, label='Humidity (%)', marker=',', linestyle='solid')
temperature_mean_line = plt.plot(date, temperature_mean, label=temperature_mean_str + ' C', marker=' ',linestyle='--')
humidity_line = plt.plot_date(date, temperature, label='Temperature (C)', marker=',', linestyle='solid')
humidity_mean_line = plt.plot(date, humidity_mean, label=humidity_mean_str + ' %', marker=' ',linestyle='--')

plt.title(label='Data Visualization', loc='left')
plt.legend()
plt.tight_layout()
plt.gcf().autofmt_xdate()

plt.show()