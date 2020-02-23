#!/usr/bin/env python3
""" Chopping vegetables with a ThreadPool """

import threading
from concurrent.futures import ThreadPoolExecutor
'''
interface for azync running tasks ratehr than working with individual threads directly
submit callable obj to threadpoolexec and it assigns them to existing threads to run asynchroniously

theadpools are commonly user to overlap io boud tasks rather than cpu intensive tasks so the number of the threads should exid the number of processors
'''

def vegetable_chopper(vegetable_id):
    name = threading.current_thread().getName()
    print(name, 'chopped vegetable', vegetable_id)

if __name__ == '__main__':
    pool = ThreadPoolExecutor(max_workers=5)
    for vegetable in range(100):
        pool.submit(vegetable_chopper, vegetable)
    pool.shutdown()  # free up any resource that the pool is using
