#!/bin/bash

# Create the s3 bucket for the code
aws s3 mb s3://aws-course-sam-bucket-hr --profile personal --region eu-west-1

# Package the template (uploads the code to s3)
aws cloudformation package --s3-bucket aws-course-sam-bucket-hr --template-file template.yaml --output-template-file gen/template-generated.yaml --profile personal --region eu-west-1

# Deploy the code
aws cloudformation deploy --template-file gen/template-generated.yaml --stack-name aws-course-sam --profile personal --region eu-west-1 --capabilities CAPABILITY_IAM

