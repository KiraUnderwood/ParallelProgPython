#!/usr/bin/env python3
""" Producers serving soup for Consumers to eat """

import queue
import threading
import time

serving_line = queue.Queue(maxsize=5)  # producer and consumer use it, queue  - for each changing obj bw mult threads

def soup_producer():
    for i in range(20): # serve 20 bowls of soup
        serving_line.put_nowait('Bowl #'+str(i))
        print('Served Bowl #', str(i), '- remaining capacity:', \
            serving_line.maxsize-serving_line.qsize())
        time.sleep(0.2) # time to serve a bowl of soup
    serving_line.put_nowait('no soup for you!')  # msg to the consumer for 2 of them since there are 2
    serving_line.put_nowait('no soup for you!')

def soup_consumer():
    while True:
        bowl = serving_line.get()
        if bowl == 'no soup for you!':  # retrieved from the q  (put_nowait) and in this case breaks and terminates the thread
            break
        print('Ate', bowl)
        time.sleep(0.3) # time to eat a bowl of soup

if __name__ == '__main__':
    for i in range(2):
        threading.Thread(target=soup_consumer).start()
    threading.Thread(target=soup_producer).start()
