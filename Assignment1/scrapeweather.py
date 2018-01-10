import pandas as pd
from pandas.io.parsers import TextParser
from datetime import datetime, timedelta, date
import logging
import sys

# LOG FILE
logger = logging.getLogger('weather')
hdlr = logging.FileHandler('weather.log')
hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)

# Logging code adapted from:
## https://docs.python.org/2.3/lib/node304.html

# GENERATE URLS TO SCRAPE
urls = []
url_base='https://www.wunderground.com/history/airport/KBOS/'
url_end='/DailyHistory.html'

# First date in Hubway data set is 7-28-11
start_date = date(2011,7,28)

# Exclude the date the script is run as weather data will be incomplete
day_count = int ((datetime.date(datetime.today()) - start_date).days)

for sd in (start_date + timedelta(n) for n in range(day_count)):
    page=url_base+sd.strftime("%Y")+'/'+sd.strftime("%m")+'/'+sd.strftime("%d")+url_end
    urls.append(page)

# Code for iterating through date range adapted from:
## https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python

logger.info('WeatherUnderground URLs generated')

# SCRAPE TABLES INTO DATA FRAMES
weatherdataframes=[]

for url in urls:
    logger.info('Scraping table from ' + url)
    dfs = pd.read_html(url, header=0)
    df = dfs[4]
    df['date']=url[50:60]
    weatherdataframes.append(df)
    logger.info('Data frame added')

# COMBINE DATA FRAMES
logger.info('Creating merged data frame')
weather = pd.DataFrame(columns = list(weatherdataframes[0]))
for df in weatherdataframes:
    weather = weather.append(df, ignore_index=True)

# WRITE CSV
logger.info('Writing csv')
weather.to_csv('weather.csv', index=False)

print('Process Complete')