from elasticsearch import Elasticsearch

def ingest(data, i):
    es = Elasticsearch(["https://localhost:9200"], basic_auth=('elastic', 'Lp9PHgG_ng3grN_ixQMi'))
    es.info()
    es.index(index='user_data', id=i, document=data)

