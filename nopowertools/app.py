import json
import logging
import os

log_level_mapping = {
  'DEBUG': logging.DEBUG,
  'INFO': logging.INFO,
  'WARN': logging.WARN,
  'ERROR': logging.ERROR
}
logger = logging.getLogger()
logger.setLevel(log_level_mapping[os.environ['LOG_LEVEL']])


def lambda_handler(event, context):
  batchItemFailures = []
  for message in event['Records']:
    logger.debug('Received message: body: ' + message['body'] + '; ApproximateReceiveCount: ' + message['attributes']['ApproximateReceiveCount'] + '; messageId: ' + message['messageId'])
    if message['body'].find("Succeed") == -1:
      batchItemFailures.append({"itemIdentifier": message['messageId']})
  
  logger.debug("batchItemFailures: " + json.dumps(batchItemFailures, indent=2))
  return {"batchItemFailures": batchItemFailures}
