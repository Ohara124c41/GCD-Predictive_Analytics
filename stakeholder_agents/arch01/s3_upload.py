import boto3
import os

import sys

access_key = ''
secret_access_key = ''



client = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)


for file in os.listdir():
    if '.json' in file:
        upload_file_bucket = 'cogent-json-test'
        upload_file_key = 'json/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)
