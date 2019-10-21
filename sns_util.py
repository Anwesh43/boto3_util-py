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

def createSubscription(sns, topicArn, protocol, endpoint):
    response = sns.subscribe(TopicArn = topicArn, Protocol = protocol, Endpoint = endpoint)
    return response['SubscriptionArn']

def listSubscriptionsByTopic(sns, topicArn):
    response = sns.list_subscriptions_by_topic(TopicArn = topicArn)
    return response['Subscriptions']

def unsubscribe(sns, subscriptionArn):
    response = sns.unsubscribe(SubscriptionArn = subscriptionArn)
    return response


sns = clientCache.get('sns')
arguments = sys.argv
twoArgsMap = {}
oneArgMap = {}
threeArgsMap = {}
twoArgsMap['createTopic'] = createTopic
twoArgsMap['deleteTopic'] = deleteTopic
twoArgsMap['listSubs'] = listSubscriptionsByTopic
twoArgsMap['unsubscribe'] = unsubscribe
oneArgMap['listTopic'] = listTopic

fourArgsMap = {}
fiveArgsMap = {}
fiveArgsMap['subscribe'] = createSubscription

if len(arguments) == 2:
    print(oneArgMap[arguments[1]](sns))

if len(arguments) == 3:
    print(twoArgsMap[arguments[1]](sns, arguments[2]))

if len(arguments) == 5:
    print(fiveArgsMap[arguments[1]](sns, arguments[2], arguments[3], arguments[4]))
