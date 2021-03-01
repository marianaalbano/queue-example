import pika
import time
from random import randrange


credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq1', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

x = 0
while True:
    time.sleep(randrange(0, 5))
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body='MESSAGE - %s' %x)
    print(" [x] Sent 'MESSAGE - %s!'" %x)
    x += 1
connection.close()