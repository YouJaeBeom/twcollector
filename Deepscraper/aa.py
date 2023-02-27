import logging
import os
from queue import Queue
from threading import Thread
from time import time
import ScrapingEngine
import multiprocessing 
import AuthenticationManager 
import time 
import socket
from itertools import repeat
import time 
import configparser
config = configparser.ConfigParser()
config.read('config.ini')


class ScrapingWorker(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        port_list = [x for x in range(10000,10200)]
        indx, query, language = self.queue.get()
        print(indx, port_list[indx], query, language)
        
        self.queue.task_done()


if(__name__ == '__main__') :
    start=time.time()
    ## query list && query index list 
    with open(config['DEFAULT']['QUERY_FILE'], 'r') as f:
        query_list = f.read().strip().split(',')
        query_index_list = [x for x in range(len(query_list))]

    with open(config['DEFAULT']['LANGUAGE_FILE'], 'r') as f:
            language_list = f.read().strip().split(',')

    queue_list = []
    for language in (language_list): 
        for query in (query_list):
            queue_list.append([query,language])
    #print(queue_list, len(queue_list))
    

    queue = Queue()
    # Create 8 worker threads
    for _ in queue_list:
        worker = ScrapingWorker(queue)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()

    # Put the tasks into the queue as a tuple
    for indx, row in enumerate(queue_list):
        queue.put((indx, row[0], row[1]))
        #queue.put((query, conn1, addr1, conn2, addr2))
    # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()

