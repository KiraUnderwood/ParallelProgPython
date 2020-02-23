#!/usr/bin/env python3
""" Chopping vegetables with a ThreadPool """

import threading
from concurrent.futures import ProcessPoolExecutor
import os
'''
threadpool exec is good for io intence tasks
but for cpu intence you need processors pool due to gil

'''
def vegetable_chopper(vegetable_id):
    name = os.getpid()
    print(name, 'chopped a vegetable', vegetable_id)

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=2) as pool:  # context mngr! now can remove shutdown method
        for vegetable in range(100):
            pool.submit(vegetable_chopper, vegetable)  # submit method returns the instance of the future class which encapsulated async exec of the callable task
