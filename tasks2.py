from __future__ import absolute_import
from kombu import Exchange, Queue
from celery import Celery
import time

app = Celery('rabbitmq',
             broker='amqp://test:test@localhost/',
             include=['tasks2'])

@app.task
def longtime_add(x, y):
    print ('long time task begins')
    time.sleep(5)
    print ('long time task finished')
    return x + y
    
@app.task
def longtime_mul(x, y) :
    print ('long time task begins')
    time.sleep(5)
    print ('long time task finished')
    return x * y

@app.task
def longtime_ok(x, y) :
    print ('long time OK begins')
    time.sleep(5)
    print ('long time OK finished')
    return x + y