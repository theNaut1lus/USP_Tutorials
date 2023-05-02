#!/bin/bash
# Create a s3 bucket
# upload a HTML page
# enable webhosting on s3
# enable public read
# start the page

bucket=demohtml-$(date "+%Y-%m-%d")-v$RANDOM

aws s3 mb s3://$bucket

aws s3 website s3://$bucket --index-document index.html

aws s3 cp index.html S3://$bucket --acl public-read

aws s3 ls

start http://$bucket.s3-website-ap-southeast-2.amazonaws.com

