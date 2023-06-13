import boto3 #to create AWS resources 

client = boto3.client('ecr')

repository_name = "cloud-monitoring-app"
response = client.create_repository(
     repositoryName=repository_name
)

repository_uri = response['repository']['repositoryUri']
print("The repository URI:",repository_uri)
