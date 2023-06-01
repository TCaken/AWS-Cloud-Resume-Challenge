import json
import boto3

client = boto3.resource('dynamodb')
table = client.Table('cakentan-cloud-resume')

def lambda_handler(event, context):
    res = table.get_item(Key={
        'record_id' : '0'
    })
    
    count = res['Item']['visitor_count']
    count = count + 1
    
    table.put_item(Item={
        'record_id' : '0',
        'visitor_count' : count,
    })

    return count