import csv
import json
csvfilepath='allbanks.csv'
jsonfilepath='prudhviallbanks.json'
data={}
with open(csvfilepath) as csvfile:
    csvreader=csv.DictReader(csvfile)
    for csvrow in csvreader:
        timestamp=csvrow['timestamp']
        data[timestamp]=csvrow
with open(jsonfilepath,'w') as jsonfile:
    jsonfile.write(json.dumps(data,indent=4))
    print(data)
