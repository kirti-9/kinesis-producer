import boto3
import json
import logging
import time
from event_record_generator import EventDataGenerator
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from config.data_stream_config import DataStreamConfig

LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


class KinesisStreamManager:
    def __init__(self, region):
        self.kinesis_client = boto3.client('kinesis', region_name=region)
        self.logger = logging.getLogger('KinesisStreamManager')

    # create_data_stream_if_not_exists checks if the desired stream is present, if not it creates one.
    def create_data_stream_if_not_exists(self, stream_name, shard_count):
        try:
            response = self.kinesis_client.describe_stream(StreamName=stream_name)
            if response['StreamDescription']['StreamStatus'] == 'ACTIVE':
                self.logger.info(f"Data stream '{stream_name}' already exists.")
                return
        except self.kinesis_client.exceptions.ResourceNotFoundException:
            pass

        # Create data stream as it doesn't exist
        try:
            self.kinesis_client.create_stream(StreamName=stream_name, ShardCount=shard_count)
            self.logger.info(f"Data stream doesn't exist, '{stream_name}' created with {shard_count} shards.")
            self.logger.info("Wait for Data stream to get provisioned")
            while True:
                response = self.kinesis_client.describe_stream(StreamName=stream_name)
                if response['StreamDescription']['StreamStatus'] == 'ACTIVE':
                    self.logger.info("Data stream status is active")
                    return
                time.sleep(1)
        except Exception as e:
            self.logger.error(f"Failed to create data stream: {e}")


class KinesisProducer:
    def __init__(self, region, stream_name):
        self.stream_name = stream_name
        self.kinesis_client = boto3.client('kinesis', region_name=region)
        self.logger = logging.getLogger('KinesisProducer')

    # push_data writes the data to an AWS Kinesis Data Stream
    def push_data(self, data, partition_key):
        try:
            self.kinesis_client.put_record(
                StreamName=self.stream_name,
                Data=json.dumps(data),
                PartitionKey=partition_key
            )
            self.logger.info("Data pushed in shard: {}".format(partition_key))
        except Exception as e:
            self.logger.error(f"Failed to push data: {e}")


def main():
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

    config = DataStreamConfig()

    # Initialize stream manager
    stream_manager = KinesisStreamManager(config.region)
    # Check if data stream exists, if not, create it
    stream_manager.create_data_stream_if_not_exists(config.stream_name, config.shard_count)

    # Initialize producer
    producer = KinesisProducer(config.region, config.stream_name)

    # Continuously push data to Kinesis stream
    while True:
        data = EventDataGenerator.generate_event_data()
        # Serialize data to JSON and then hash for equal data distribution
        partition_key = str(hash(json.dumps(data)))
        producer.push_data(data, partition_key)
        time.sleep(1)  # to push 1 record per second


if __name__ == "__main__":
    main()
