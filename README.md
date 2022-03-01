# aws-lambda-powertools-poc

This repository contains a SAM CloudFormation template which demos 2 different ways to return batch item failures

The ./nopowertools Lambda does not utilise AWS Lambda Powertools
The ./powertoosl Lambda does. :)

# Steps to deploy

1. Deploy SAM template
2. update publish.sh with SNS topic ARN
3. run `./publish.sh`
