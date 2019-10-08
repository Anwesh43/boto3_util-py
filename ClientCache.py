import boto3
class ClientCache:
    def __init__(self):
        region = 'us-east-1'
        self.clientMap = {}
        self.clientMap['s3'] = boto3.client('s3', region_name = region)
        self.clientMap['sns'] = boto3.client('sns', region_name = region)

    def get(self, clientType):
        return self.clientMap[clientType]

clientCache = ClientCache()
