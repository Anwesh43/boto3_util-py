from ClientCache import clientCache
import sys
import codecs

s3 = clientCache.get('s3')

def upload(s3, bucketName, fileName, keyName):
    resp = s3.upload_file(Filename = fileName, Bucket = bucketName, Key = keyName)
    print(resp)
    print('uploaded {0} to s3 bucket {1}'.format(fileName, bucketName))

def list(s3, bucketName, maxKey, prefix):
    resp = s3.list_objects(Bucket = bucketName, MaxKeys = int(maxKey), Prefix = prefix)
    print(resp['Contents'])

def download(s3, bucketName, fileName, keyName):
    resp = s3.download_file(Filename = fileName, Bucket = bucketName, Key = keyName)
    print(resp)
    print('downloaded the file {0}'.format(fileName))

def delete(s3, bucketName, key):
    resp = s3.delete_object(Bucket = bucketName, Key = key)
    print(resp)
    print('deleted {0}'.format(key))

def put_acl(s3, bucketName, key, accessType):
    s3.put_object_acl(Bucket = bucketName, Key = key, ACL = accessType)
    print("successfully change access to {0} to {1}".format(key, accessType))

def getobject(s3, bucketName, key):
    obj = s3.get_object(Bucket = bucketName, Key = key)
    body = obj['Body']
    print(body)
    for ln in codecs.getreader('utf-8')(body):
        print(ln)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        operation = sys.argv[1]
        opMap = {}
        opMap['list'] = list
        opMap['download'] = download
        opMap['upload'] = upload
        opMap['delete'] = delete
        opMap['putacl'] = put_acl
        opMap['getobject'] = getobject
        if operation in opMap:
            if len(sys.argv) == 4:
                opMap[operation](s3, sys.argv[2], sys.argv[3])
            else:
                opMap[operation](s3, sys.argv[2], sys.argv[3], sys.argv[4])
        else:
            print("operation doesn't exist")
    else:
        print("enter all details")
