import json
import logging
import os
from aws_lambda_powertools.utilities.batch import BatchProcessor, EventType, batch_processor
from aws_lambda_powertools.utilities.data_classes.sqs_event import SQSRecord

log_level_mapping = {
  'DEBUG': logging.DEBUG,
  'INFO': logging.INFO,
  'WARN': logging.WARN,
  'ERROR': logging.ERROR
}
logger = logging.getLogger()
logger.setLevel(log_level_mapping[os.environ['LOG_LEVEL']])

processor = BatchProcessor(event_type=EventType.SQS)

def record_handler(record: SQSRecord):
  payload: str = record.body
  logger.debug(f'Received message: body: {payload}; ApproximateReceiveCount: {record.attributes.approximate_receive_count}; messageId: {record.message_id}')
  if payload.find('Succeed') == -1:
    raise Exception('failed to process message')

@batch_processor(record_handler=record_handler, processor=processor)
def lambda_handler(event, context):
  return processor.response()
