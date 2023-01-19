import csv
import json

def read__csv(csvfilepath):
    data={}
    with open('allbanks.csv') as csvfile:
        csvreader=csv.DictReader(csvfile)
    for csvrow in csvreader:
        timestamp=csvrow['timestamp']
        data[timestamp]=csvrow
def write_to_json(jsonfilepath):
    with open('rameshallbanks.json','w') as jsonfile:
        jsonfile.write(json.dumps(data,indent=4))
        
        
def main():
    data=read_csv(allbanks.csv)
    write_to_json(rameshallbanks.json)
    if __name_=='__main__':
        main()


        

    
  







    
       
