# Serialize ImageData

import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    key = event["s3_key"]
    bucket = event["s3_bucket"]
    
    s3.download_file(bucket, key, "/tmp/image.png")
    
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())
        
    print("Event:", event.keys())
    
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }}


# Image Classification

import json
import base64
import boto3
import os

ENDPOINT = 'image-classification-2023-04-01-12-15-33-248'

runtime = boto3.client('runtime.sagemaker')


def lambda_handler(event, context):
    region = os.environ['AWS_REGION']
    print(region)
    image = base64.b64decode(event["image_data"])
    
    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT, 
        ContentType='image/png', 
        Body=image
        )
    
    inferences = json.loads(response['Body'].read().decode('utf-8'))
    
    event['inferences'] = inferences
    
    return {
        'statusCode': 200,
        'body': event
    }


import json

THRESHOLD = 0.70

# Filter Result

def lambda_handler(event, context):
    

    inferences = event['inferences']
    

    meets_threshold = max(inferences) > THRESHOLD     
    
    if meets_threshold:
        pass
    else:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': event  
    }




