class DataStreamConfig:
    def __init__(self):
        # name of AWS Kinesis DataStream
        self.stream_name = 'AForB_callevents'
        # aws region where the data stream is to be created/read from.
        self.region = 'eu-north-1'
        # number of shards in the data stream
        self.shard_count = 4
