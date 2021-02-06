import json

import boto3
from aws_xray_sdk.core import patch_all, xray_recorder

patch_all()

S3 = boto3.client("s3")
BUCKET_NAME = "xrayinvestigation"


def lambda_handler(event, context):
    raw_data = S3.get_object(Bucket=BUCKET_NAME, Key="sample_data.json")
    data = json.loads(raw_data["Body"].read())
    with xray_recorder.in_subsegment("Throwing exception") as subsegment:
        subsegment.put_metadata("very_important_inforamtion", {"message": "Hello I am metadata"}, "information")
        subsegment.put_annotation("very_important_annotation", "Very very important information")
        raise Exception("Information")
    return {
        "statusCode": 200,
        "body": data["message"]
    }
