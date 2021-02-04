from .tasks import longtime_add
import time
import kombu

if __name__ == '__main__':
    result = longtime_add.apply_async((1,2), exchange='default', routing_key='moon')
    # at this time, our task is not finished, so it will return False
    print ('Task finished? ', result.ready())
    print ('Task result: ', result.result)
    # sleep 10 seconds to ensure the task has been finished
    time.sleep(10)
    # now the task should be finished and ready method will return True
    print ('Task finished? ', result.ready())
    print ('Task result: ', result.result)