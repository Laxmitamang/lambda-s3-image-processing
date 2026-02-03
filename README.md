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
