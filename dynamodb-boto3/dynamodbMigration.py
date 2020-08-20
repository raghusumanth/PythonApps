import boto3
import os
#db1_accessKey,db1_secretKey,db2_accessKey,db1_secretKey should be added as environment variables
# Source table creds - prod acc
Accesskey             = os.getenv('db1_accessKey')
SecreateAccesskey     = os.getenv('db1_secretKey')

dynamodb              = boto3.resource('dynamodb',
                                        region_name='ap-south-1',

endpoint_url="https://dynamodb.ap-south-1.amazonaws.com",
                                        aws_access_key_id=Accesskey,
                                        aws_secret_access_key=SecreateAccesskey)


# destination table creds - dev acc
Accesskey_dev         = os.getenv('db2_accessKey')
SecreateAccesskey_dev = os.getenv('db2_secretKey')

dynamodb_destination  = boto3.resource('dynamodb',
region_name='ap-south-1',
endpoint_url="https://dynamodb.ap-south-1.amazonaws.com",
aws_access_key_id=Accesskey_dev,
aws_secret_access_key=SecreateAccesskey_dev)


table             = dynamodb.Table('db1_tablename') # source table name
table_destination = dynamodb_destination.Table('db2_tablename') #
destination table name
print(table.creation_date_time)
print(table_destination.creation_date_time)
#print(table.list_tables())
print('Connection successful')
response = table.scan()
items    = response['Items']

print('record cnt',items)
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

for record in items:
    with table_destination.batch_writer() as batch:
        batch.put_item(Item=record)