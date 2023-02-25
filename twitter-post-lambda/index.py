import json
import requests

def lambda_handler(event, context):
	print("Pre Request")
	r = requests.get('https://www.google.co.uk/')
	print("Post Request")
	return {'statusCode': 200,'body': json.dumps('Hello from Lambda!')}