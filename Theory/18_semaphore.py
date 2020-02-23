#!/usr/bin/env python3
""" Connecting cell phones to a charger """

import random
import threading
import time

charger = threading.Semaphore(1)  # binary symaphore ~ mutex, can be chnaged to 4

def cellphone():
    name = threading.current_thread().getName()
    with charger:  # context mngr instead of explicit aquire/release
        print(name, 'is charging...')
        time.sleep(random.uniform(1,2))
        print(name, 'is DONE charging!')

if __name__ == '__main__':
    for i in range(10):
        threading.Thread(target=cellphone, name='Phone-'+str(i)).start()
