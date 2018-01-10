import zipfile
import requests
from io import StringIO,BytesIO
import pandas as pd
import logging
import sys

# LOG FILE
logger = logging.getLogger('hubway')
hdlr = logging.FileHandler('hubway.log')
hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)

# Logging code adapted from:
## https://docs.python.org/2.3/lib/node304.html

# GENERATE URLS TO SCRAPE
# The data set is on AWS in two formats
# Data prior to 2015 is in annual csv files
# Data starting with 2015 is in monthly zip files
url_base='https://s3.amazonaws.com/hubway-data/'
years=['2015','2016','2017']
csv_list=['hubway_Trips_2011.csv','hubway_Trips_2012.csv','hubway_Trips_2013.csv','hubway_Trips_2014_1.csv','hubway_Trips_2014_2.csv']
url_zip_end='-hubway-tripdata.zip'
urls_csv=[]
urls_zip=[]

for c in csv_list:
    urls_csv.append(url_base + c)

logger.info('CSV URLs generated')

for yr in years:
    for i in range(1,13):
        if(i >=10):
            urls_zip.append(url_base + str(yr) + str(i) + url_zip_end)
        else:
            urls_zip.append(url_base + str(yr) + '0' +str(i) + url_zip_end)

logger.info('Zip file URLs generated')

# SCRAPE FILES INTO DATA FRAMES AND WRITE TO CSV
dataframe_collection_0=[]
dataframe_collection_1=[]

# Data prior to 2015
for url in urls_csv:
    logger.info('Reading csv from ' + url)
    st = pd.read_csv(url, header=0)
    dataframe_collection_0.append(st)
    logger.info('Data frame added')

logger.info('Creating merged data frame')
columns0 = list(dataframe_collection_0[0])
frame0 = pd.DataFrame(columns=columns0)

for df in dataframe_collection_0:
    frame0 = frame0.append(df, ignore_index=True)

logger.info('Writing csv')

frame0.to_csv('pre2015.csv')


# 2015 and after
for url in urls_zip:
    logger.info('Reading csv from ' + url)
    try:
        r = requests.get(url, stream=True)
        z = zipfile.ZipFile(BytesIO(r.content))
        st = pd.read_csv(z.open(url[37:60]+'csv'), header=0)
        dataframe_collection_1.append(st)
        logger.info('Data frame added')
    except:
        logger.warning('file not found')

logger.info('Creating merged data frame')
columns1 = list(dataframe_collection_1[0])
frame1 = pd.DataFrame(columns=columns1)

for df in dataframe_collection_1:
    frame1 = frame1.append(df, ignore_index=True)

logger.info('Writing csv')
frame1.to_csv('2015-2017.csv')

print('Process Complete')