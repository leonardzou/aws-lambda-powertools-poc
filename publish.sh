# bash script to publish a bunch of messages to SNS topic
aws sns publish-batch \
  --topic-arn "arn:aws:sns:us-west-2:123456789012:sns-topic-name" \
  --publish-batch-request-entries file://messages.json \
  --region us-west-2
