import boto3
from ClientCache import clientCache
import sys

def createTopic(sns, topicName):
    response = sns.create_topic(Name = topicName)
    return response['TopicArn']

def listTopic(sns):
    response = sns.list_topics()
    return response['Topics']

def deleteTopic(sns, topicArn):
    response = sns.delete_topic(TopicArn = topicArn)
    return response


sns = clientCache.get('sns')
arguments = sys.argv
twoArgsMap = {}
oneArgMap = {}
threeArgsMap = {}
twoArgsMap['createTopic'] = createTopic
twoArgsMap['deleteTopic'] = deleteTopic
oneArgMap['listTopic'] = listTopic

if len(arguments) == 2:
    print(oneArgMap[arguments[1]](sns))

if len(arguments) == 3:
    print(twoArgsMap[arguments[1]](sns, arguments[2]))
