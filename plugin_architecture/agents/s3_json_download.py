import boto3

access_key = 'AKIA2B2CNOEEV5C6OCVY'
secret_access_key = ''


client = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)
                        
with open('ARCH01.json', 'wb') as f:
    client.download_fileobj('cogent-json-test', 'json/ARCH01.json', f)
