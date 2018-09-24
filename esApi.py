import requests
from printer import pr

# curl -X PUT "localhost:9200/twitter"
def createIndex(newIndexName='new_index_name', elasticSearchUrl='http://localhost:9200/'):
    return requests.put(elasticSearchUrl + newIndexName)
     
# bulk docmument index from json
# curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/_bulk --data-binary "@requests"; 
# echo {"took":7, "errors": false, "items":[{"index":{"_index":"test","_type":"_doc","_id":"1","_version":1,"result":"created","forced_refresh":false}}]}
def bulkIndex(indexName, documents, elasticSearchUrl='http://localhost:9200/'):
    return requests()

# curl -X DELETE "localhost:9200/twitter"
def deleteIndex(indexName, elasticSearchUrl='http://localhost:9200/'):
    return requests.delete(elasticSearchUrl + indexName)



