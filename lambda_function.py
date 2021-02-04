import json

import boto3
from aws_xray_sdk.core import patch_all

patch_all()

S3 = boto3.client("s3")
BUCKET_NAME = "xrayinvestigation"


def lambda_handler(event, context):
    raw_data = S3.get_object(Bucket=BUCKET_NAME, Key="sample_data.json")
    data = json.loads(raw_data["Body"].read())
    return {
        "statusCode": 200,
        "body": data["message"]
    }
