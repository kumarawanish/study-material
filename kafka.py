from confluent_kafka import Producer, KafkaError, KafkaException
import json
import time

conf = {
    'bootstrap.servers': '127.0.0.1:9092',
    'client.id': 'producer-api-server'
}

producer = Producer(conf)

connected = False

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def on_producer_disconnect(error):
    if error.code() == KafkaError._PARTITION_EOF:
        # End of partition event, not an actual error
        return

    print(f'Producer disconnected: {error}')

    global connected
    connected = False

producer.poll(0)  # Required to handle events

def publish(topic, partition_key, data, meta):
    global connected
    value = {'meta': {**meta, 'ts': int(time.time() * 1000)}, 'data': data}
    
    try:
        if not connected:
            producer.connect()
            connected = True

        print('kafka publish', topic, partition_key, value)

        producer.produce(
            topic=f'api-server.{topic}',
            key=partition_key.encode('utf-8'),
            value=json.dumps(value).encode('utf-8'),
            callback=delivery_report
        )

        # Wait for any outstanding messages to be delivered
        producer.poll(0)

    except KafkaException as e:
        print(e)

# Example usage:
publish('your_topic', 'your_partition_key', {'your_data_key': 'your_data_value'}, {'your_meta_key': 'your_meta_value'})
