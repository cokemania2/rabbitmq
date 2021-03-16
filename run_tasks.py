from __future__ import absolute_import
from tasks2 import *
import kombu

if __name__ == '__main__':
    for i in range(1) :
        result = longtime_add.apply_async((1,2), queue='moon')
        # result2 = longtime_mul.apply_async((1,2), queue='sunshine')
        # result3 = longtime_ok.apply_async((0,0))