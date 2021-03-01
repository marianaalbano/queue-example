import pika
import time
from random import randrange
import logging


log = logging.getLogger("my-logger")

credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq1', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')
def callback(ch, method, properties, body):
    log.info(" [x] Received %r" % body)
    time.sleep(randrange(0, 5))
    log.info("[x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume('hello',
                      callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()