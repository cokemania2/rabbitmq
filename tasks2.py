from __future__ import absolute_import
from kombu import Exchange, Queue
from celery import Celery
import time

default_exchange_name = 'default'

default_queue_name = 'default'
default_routing_key = 'default'

sunshine_queue_name = 'sunshine'
sunshine_routing_key = 'sunshine'

moon_queue_name = 'moon'
moon_routing_key = 'moon'

app = Celery('rabbitmq',
             broker='amqp://test2:test2@localhost/',
             routing_key=default_routing_key,
             include=['tasks2'])

default_exchange = Exchange(default_exchange_name, type='direct')
default_queue = Queue(
    default_queue_name,
    default_exchange,
    routing_key=default_routing_key)

sunshine_queue = Queue(
    sunshine_queue_name,
    default_exchange,
    routing_key=sunshine_routing_key)

moon_queue = Queue(
    moon_queue_name,
    default_exchange,
    routing_key=moon_queue_name)

app.conf.task_queues = (default_queue, sunshine_queue, moon_queue)

app.conf.task_default_queue = default_queue_name
app.conf.task_default_exchange = default_exchange_name
app.conf.task_default_routing_key = default_routing_key

@app.task
def longtime_add(x, y):
    print ('long time task begins')
    # sleep 5 seconds
    time.sleep(5)
    print ('long time task finished')
    return x + y
    
@app.task
def longtime_mul(x, y) :
    print ('long time task begins')
    # sleep 5 seconds
    time.sleep(5)
    print ('long time task finished')
    return x * y

@app.task
def longtime_ok(x, y) :
    print ('long time OK begins')
    # sleep 5 seconds
    time.sleep(5)
    print ('long time OK finished')
    return x + y