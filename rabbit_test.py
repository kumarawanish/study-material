import pika
import json
import logging

class RabbitMQ:
    def __init__(self, config):
        self.conn_string = config['conn_string']
        self.queue = config['queue_name']

    async def connect(self):
        try:
            self.connection = await pika.AsyncioConnectionParameters(self.conn_string)
            self.channel = await self.connection.channel()
            await self.channel.queue_declare(queue=self.queue, durable=False)
            return {'success': True}

        except Exception as err:
            logging.error(f"{err.__class__.__name__}: {str(err)}")
            return {'error': str(err)}

    async def send(self, data):
        try:
            self.channel.basic_publish(exchange='',
                                       routing_key=self.queue,
                                       body=json.dumps(data))
            return {'success': True}

        except Exception as err:
            logging.error(f"{err.__class__.__name__}: {str(err)}")
            return {'error': str(err)}

    async def receive(self):
        try:
            return await self._consume()

        except Exception as err:
            logging.error(f"{err.__class__.__name__}: {str(err)}")
            return {'error': str(err)}

    async def _consume(self):
        return await self.channel.basic_get(queue=self.queue, auto_ack=True)

    async def disconnect(self):
        await self.channel.close()
        await self.connection.close()

# Usage example:
# config = {'conn_string': 'amqp://guest:guest@localhost:5672/', 'queue_name': 'my_queue'}
# rabbitmq = RabbitMQ(config)
# await rabbitmq.connect()
# await rabbitmq.send({'key': 'value'})
# received_message = await rabbitmq.receive()
# print(received_message)
# await rabbitmq.disconnect()
