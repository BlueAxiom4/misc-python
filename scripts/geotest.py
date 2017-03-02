import sys
import pandas as pd
from urllib2 import Request, urlopen
import json
from pandas.io.json import json_normalize



path1 = '42.974049,-81.205203|42.974298,-81.195755'
myurl= 'http://maps.googleapis.com/maps/api/elevation/json?locations='+path1+'&sensor=false'
# request=Request('http://maps.googleapis.com/maps/api/elevation/json?locations='+path1+'&sensor=false')
# response = urlopen(request)
# elevations = response.read()
# data = json.loads(elevations)
# json_normalize(data['results'])

df = pd.read_json(myurl)
print df