# AWS Lambda – S3 Image Processing with SNS Alerts

## Project Overview
This project demonstrates an AWS serverless workflow where an AWS Lambda
function is triggered by S3 object uploads. Image files are automatically
moved to a destination bucket, and an SNS email notification is sent for
successful processing.

## Architecture
- Amazon S3 (source bucket trigger)
- AWS Lambda (Python)
- Amazon SNS (email notifications)
- IAM (least privilege)

## Workflow
1. User uploads a file to the source S3 bucket
2. Lambda is triggered by S3 event
3. Lambda validates file type
4. Images (.jpg, .png) are moved to destination bucket
5. Non-image files remain untouched
6. SNS sends an email notification

## IAM Security
The Lambda execution role uses least-privilege permissions:
- Read objects from source bucket
- Write objects to destination bucket
- Publish messages to SNS topic
- CloudWatch logging

## Testing
- Uploaded `.jpg` → moved successfully
- Uploaded `.pdf` → remains in source bucket
- SNS email received on success

## Files
- `lambda_function.py` – Lambda logic
- `iam-policy.json` – Least privilege IAM policy

## Future Improvements
- Add CloudWatch alarms
- Add image size validation
- Add tagging for processed objects


## IAM Least Privilege Policy

The Lambda function uses a custom IAM execution role with minimum permissions:

- Read objects from the source S3 bucket
- Write objects to the destination S3 bucket
- Publish alerts to an SNS topic
- Write logs to CloudWatch

The policy JSON is available in:
`iam-policy/iam-least-privilege-policy.json`

## SNS Notifications

An Amazon SNS topic is used to send email notifications when:

- An image is successfully moved to the destination bucket
- An error occurs during Lambda execution

The SNS topic configuration is documented in:
`SNS/sns-topic.json`

Email was chosen over SMS to avoid additional costs and remain within the AWS Free Tier.

