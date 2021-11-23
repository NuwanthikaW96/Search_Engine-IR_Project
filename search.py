import app
from elasticsearch import Elasticsearch
import json

es = Elasticsearch()

def search_text_multi_match_query(input,fields):
    print("multi_match_query")
    result=es.search(index="male-cricketers-data",body={
        	"query": {
        		"multi_match": {
        			"query": input,
        			"fields": fields,
        			"operator": 'and',
        			"type": "cross_fields"
        		}
        	},
                "aggs": {
        		"Name_En": {
        			"terms": {
        				"field": "nameEn.keyword",
        				"size": 20
        			}
        		},
        		"Name_Si": {
        			"terms": {
        				"field": "nameSi.keyword",
        				"size": 20
        			}
        		},
        		"Country": {
        			"terms": {
        				"field": "country.keyword",
        				"size": 20
        			}
        		},
                "Playing Role": {
        			"terms": {
        				"field": "playingRole.keyword",
        				"size": 20
        			}
        		},
                "Batting Style": {
        			"terms": {
        				"field": "battingStyle.keyword",
        				"size": 20
        			}
        		},
                "Bowling Style": {
        			"terms": {
        				"field": "bowlingStyle.keyword",
        				"size": 20
        			}
        		},
        	}
        })
    for key, value in result.items():
           if key=="aggregations":
                for key, value in value.items():
                    print(key)
    print(result)
    return result

def es_wildcard_query(fields,term1,term2):
    print("Wildcard Elasticsearch Query")
    word=term1+"*"+term2
    result=es.search(index="male-cricketers-data",body={
        "query": {
            "query_string": {
                "query": word,
        		"fields": fields,
				
            }
        },
		"aggs": {
        		"Name_En": {
        			"terms": {
        				"field": "nameEn.keyword",
        				"size": 20
        			}
        		},
        		"Name_Si": {
        			"terms": {
        				"field": "nameSi.keyword",
        				"size": 20
        			}
        		},
        		"Country": {
        			"terms": {
        				"field": "country.keyword",
        				"size": 20
        			}
        		},
                "Playing Role": {
        			"terms": {
        				"field": "playingRole.keyword",
        				"size": 20
        			}
        		},
                "Batting Style": {
        			"terms": {
        				"field": "battingStyle.keyword",
        				"size": 20
        			}
        		},
                "Bowling Style": {
        			"terms": {
        				"field": "bowlingStyle.keyword",
        				"size": 20
        			}
        		},
		}
    })
    print(result)
    return result

        