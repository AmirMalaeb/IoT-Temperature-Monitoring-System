import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TemperatureData')
sns = boto3.client('sns')
topic_arn = 'arn:aws:sns:YOUR_REGION:YOUR_ACCOUNT_ID:TemperatureAlerts'

def process_record(record):
    try:
        sns_message = record.get('Sns', {}).get('Message', '{}')
        print("SNS Message:", sns_message)
        
        payload = json.loads(sns_message)
        print("Payload:", payload)
        
        temperature = Decimal(str(payload.get('temperature', '0')))
        if 'sensor_id' not in payload or 'timestamp' not in payload:
            raise ValueError("Invalid payload: 'sensor_id' or 'timestamp' missing")
        
        table.put_item(
            Item={
                'sensor_id': payload['sensor_id'],
                'timestamp': payload['timestamp'],
                'temperature': temperature
            }
        )
        print("Data inserted into DynamoDB:", payload)
        
        if temperature > 30:
            sns.publish(
                TopicArn=topic_arn,
                Message=f"High temperature alert! Sensor: {payload['sensor_id']}, Temperature: {temperature}"
            )
            print("SNS alert sent.")
            
    except Exception as e:
        print(f"Error processing record: {record}")
        print(e)

def lambda_handler(event, context):
    print("Received event:", json.dumps(event, indent=2))
    
    if 'Records' in event:
        for record in event['Records']:
            process_record(record)
    else:
        try:
            process_record({'Sns': {'Message': json.dumps(event)}})
        except Exception as e:
            print(f"Error processing direct event: {event}")
            print(e)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data processed successfully')
    }