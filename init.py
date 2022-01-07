from elasticsearch import Elasticsearch
es = Elasticsearch()


res = es.index(index='my-words', document={'value': 'elasticsearch'})
print(res)