import pika
import time
from random import randrange

credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq1', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(randrange(0, 5))
    print(" [x] ERROR")
    ch.basic_nack(delivery_tag = method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume('hello',
                      callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()