import boto3
from io import StringIO
from config.config import AWS_BUCKET_NAME

def upload_to_s3(df, filename):
    s3_client = boto3.client('s3')
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3_client.put_object(Bucket=AWS_BUCKET_NAME, Key=filename, Body=csv_buffer.getvalue())
