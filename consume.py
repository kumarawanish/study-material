import pika

# Connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Set up the consumer to use the callback function
channel.basic_consume(queue='my_queue', on_message_callback=callback) # Consume on this basis of particular queue name

print(' [*] Waiting for messages. To exit, press CTRL+C')
# Start consuming messages
channel.start_consuming()