from __future__ import absolute_import
from tasks2 import *
import kombu

if __name__ == '__main__':
    for i in range(30) :
        result = longtime_add.apply_async((1,2))
        result2 = longtime_mul.apply_async((1,2))
        result3 = longtime_ok.apply_async((0,0))