import csv
import json
data={}


def read_csv(csvfilepath):
    with open('allbanks.csv') as csvfile:
        csvreader=csv.DictReader(csvfile)
        for csvrow in csvreader:
            timestamp=csvrow['timestamp']
            data[timestamp]=csvrow
def write_json(jsonfilepath):
    with open('rameshallbanks.json','w') as jsonfile:
        jsonfile.write(json.dumps(data,indent=4))
def main():
    read_csv('allbanks.csv')
    write_json('rameshallbanks.csv')
if __name__=='__main__':
    main()
    print(data)

   

     
   

    
    



  


    
    
  
    
    

        
    
    
    
        
    








    
       
