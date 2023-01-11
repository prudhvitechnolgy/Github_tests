import csv
import json
def read_from_csv(csvfilepath):
    
    csvfilepath='allbanks.csv'
    

data={}

with open('allbanks.csv') as csvfile:
    csvreader=csv.DictReader(csvfile)
    for csvrow in csvreader:
        timestamp=csvrow['timestamp']
        data[timestamp]=csvrow
def write_to_json(jsonfilepath):
    jsonfilepath='prudhviallbanks.json'
    
with open('prudhviallbanks.json','w') as jsonfile:
    
    jsonfile.write(json.dumps(data,indent=4))
    print(data)




        



          
        





        


            
        

