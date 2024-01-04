import pika

# Connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Create a queue
channel.queue_declare(queue='my_queue')

# Publish a message
channel.basic_publish(exchange='', routing_key='my_queue', body='Hello, RabbitMQ!')
channel.basic_publish(exchange='', routing_key='my_queue', body='Welcome to my show!')

print(" [x] Sent!!!!!!!!!")

# Close the connection
connection.close()


