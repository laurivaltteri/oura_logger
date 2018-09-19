# playground script to test the data access
import requests, csv
import json
from datetime import date, timedelta, datetime
import dateutil.parser
# ISO 8601 time format = "%Y-%m-%dT%H:%M:%S%z"

# get the access_token from config file


# get user information (all of us are 40 yrs old males)
url = "https://api.ouraring.com/v1/userinfo?access_token="+config.TOKEN
response = requests.get(url)
response.json()

# get last week sleep summary
daycount = 7
lastdate = str(date.today() - timedelta(days=daycount))
nowdate = str(date.today())

url = "https://api.ouraring.com/v1/sleep?start=" + \
    lastdate + "&end=" + nowdate + "&access_token=" + config.TOKEN

response = requests.get(url)
parsed = response.json()
parsed['sleep'][0]['bedtime_start'][0:10] # check that the data is loaded
#parsed['sleep'][0].keys() # check the keys for the data fetched

# function to calculate time of sleep midpoint
def bedtime_midpoint(data):
    for item in data:
        start = dateutil.parser.parse(item['bedtime_start'])
        mid_sec = timedelta(seconds=item['midpoint_time'])
        yield (start + mid_sec).isoformat()

# list the midpoints of the sleep
list(bedtime_midpoint(parsed['sleep']))

# loop that prints average HR for each night
for item in parsed['sleep']:
    print(item['bedtime_start'][0:10]+': '+str(item['hr_average']))
