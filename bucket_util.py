import sys
from ClientCache import clientCache
s3 = clientCache.get('s3')

def list_buckets(s3):
    buckets = s3.list_buckets()
    print(buckets['Buckets'])

def create_bucket(s3, bucketName):
    s3.create_bucket(Bucket = bucketName)
    print('created bucket {0}'.format(bucketName))

def delete_bucket(s3, bucketName):
    s3.delete_bucket(Bucket = bucketName)
    print('deleted bucket {0}'.format(bucketName))

opMap = {}
opMap['list'] = list_buckets
opMap['create'] = create_bucket
opMap['delete'] = delete_bucket
if len(sys.argv) >= 2:
    operation = sys.argv[1]
    if operation in opMap:
        if len(sys.argv) == 2:
            opMap[operation](s3)
        else:
            opMap[operation](s3, sys.argv[2])
    else:
        print('enter a valid operation')

else:
    print('please enter operation name and bucket name if required')
