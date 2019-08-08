import boto3
import botocore
import json

def lambda_handler(event, context):
    
    #get s3 url from event dictionary
    image_file = 'C:\Temp\aws\sample.jpeg'
    # bucket = 'shoofping-demo'

    #pass it to the aws rekognition api
    r_client = boto3.client('rekognition')
    with open(image_file, 'rb') as image:
        response = r_client.detect_faces(Image={'Bytes': image.read()}, Attributes=['ALL'])
        # response = r_client.detect_faces(Image={'S3Object': {'Bucket': bucket , 'Name': file_name}}, Attributes=['ALL'])

    for faceDetail in response['FaceDetails']:
        print('The detected face is between ' + str(faceDetail['AgeRange']['Low']) 
              + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
        print('Here are the other attributes:')
        print(json.dumps(faceDetail, indent=4, sort_keys=True))

    pass


