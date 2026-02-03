import boto3
import urllib.parse

s3 = boto3.client('s3')
sns = boto3.client('sns')

SOURCE_BUCKET = "SOURCE-BUCKET"
DESTINATION_BUCKET = "DEST-BUCKET"
SNS_TOPIC_ARN = "YOUR-SNS-TOPIC-ARN"

def lambda_handler(event, context):

    record = event['Records'][0]
    bucket_name = record['s3']['bucket']['name']
    object_key = urllib.parse.unquote_plus(
        record['s3']['object']['key']
    )

    print(f"File uploaded: {object_key}")

    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')

    if not object_key.lower().endswith(image_extensions):
        print("Not an image. Ignoring.")
        return

    try:
        s3.copy_object(
            Bucket=DESTINATION_BUCKET,
            CopySource={
                'Bucket': SOURCE_BUCKET,
                'Key': object_key
            },
            Key=object_key
        )

        s3.delete_object(
            Bucket=SOURCE_BUCKET,
            Key=object_key
        )

        message = f"Image '{object_key}' moved from {SOURCE_BUCKET} to {DESTINATION_BUCKET}"

        sns.publish(
            TopicArn="YOUR-SNS-TOPIC-ARN",
            Subject="Image Moved Successfully",
            Message=message
        )

        print("SNS notification sent.")

    except Exception as e:
        sns.publish(
            TopicArn="YOUR-SNS-TOPIC-ARN",
            Subject="Lambda Image Move FAILED",
            Message=str(e)
        )
        raise
