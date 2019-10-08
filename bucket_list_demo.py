import boto3
from ClientCache import clientCache
s3 = clientCache.get('s3')
buckets = s3.list_buckets()
print(buckets['Buckets'])
