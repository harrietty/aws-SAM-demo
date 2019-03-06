import json

print('Loading function')

def lambda_handler(event, context):
    print("value1=" + event["key1"])
    print("value2=" + event["key2"])
    return "Finished doing lambda stuff v2"
