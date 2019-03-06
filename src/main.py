import json
import boto3
import os

# Create client outside of handler for best performance

region_name = os.environ['REGION_NAME']
dynamo = boto3.client('dynamodb', region_name=region_name)
table_name = os.environ['TABLE_NAME']

def lambda_handler(event, context):
    result = dynamo.scan(TableName=table_name)
    return {
            'statusCode': '200',
            'body': json.dumps(result),
            'headers': {'Content-Type': 'application/json'}
            }
