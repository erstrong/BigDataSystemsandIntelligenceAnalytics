import pandas as pd
import logging
#import requests
import urllib.request

# LOG FILE
logger = logging.getLogger('actors')
hdlr = logging.FileHandler('actors.log')
hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)

# Logging code adapted from:
## https://docs.python.org/2.3/lib/node304.html


# READ CSV
actors = pd.read_csv('actors.csv', header=0)
print(actors.head())

counter = 0

for index,row in actors.iterrows():
    
    
    location = 'training-images/facescrub/'+row.directory+'/'+row.directory+str(index)+'.jpg'
    
    try:
        urllib.request.urlretrieve(row.url, location)
        logger.info(location + ' added')
        counter += 1
    except Exception as e:
        logger.warning(row.url + ' not found, error: ' + str(e))






