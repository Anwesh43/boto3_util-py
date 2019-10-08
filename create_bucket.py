import boto3
import sys
from ClientCache import clientCache
if len(sys.argv) == 2:
    bucket_name = sys.argv[-1]
    clientCache.get('s3').create_bucket(Bucket = bucket_name)
    print('bucket {0} created'.format(bucket_name))
