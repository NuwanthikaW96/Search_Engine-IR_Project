from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json,re
# import queries
client = Elasticsearch(HOST="http://localhost",PORT=9200)
INDEX = 'male-cricketers'

index = Index(INDEX,using=client)
res = index.create()
print (res)
    
with open('Corpus/cricketers.json','r') as f:
        cricketers = json.loads(f.read())
        for i in range(len(cricketers)):            
            y = json.dumps(cricketers[i])
            z=json.loads(y)
            print(z)
                
            e={
                "nameEn" :  z["Name_En"],
                "nameSi" : z["Name_si"],
                "fullName" : z["Full Name"],
                "country" : z["Country"],
                "dateOfBirth": z["Date of Birth"],
                "playingRole": z["Playing Role"],
                "battingStyle":z["Batting Style"],
                "bowlingStyle": z["Bowling Style"],
                "teams":z["Teams"],
                "profile":z["Profile"]


            }
            print(e)
            res=client.index(index=INDEX,id=i,body=e)
            print (res)
        
