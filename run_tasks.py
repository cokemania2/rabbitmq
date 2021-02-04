from .tasks import longtime_add, longtime_mul
import time
import kombu

if __name__ == '__main__':
    for i in range(100) :
        result = longtime_add.apply_async((1,2), queue='moon')
        result2 = longtime_mul.apply_async((1,2), queue='sunshine')