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
import random

class ScrapingWorker(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        #port = random.randint(10000,10200)
        query, x_guest_token = self.queue.get()

        streamscraper = ScrapingEngine.ScrapingEngine(query, x_guest_token)
        streamscraper.start_scraping()        
        self.queue.task_done()


if __name__ == '__main__':
    start=time.time()

    tweetIDfile = 'tweetID/tweetID.txt'
    if os.path.exists(tweetIDfile ):
        os.remove(tweetIDfile)
        print("The file has been deleted successfully")
    else:
        print("The file does not exist!")
        os.makedirs(os.path.dirname(tweetIDfile), exist_ok=True)

    query_list =[]
    query_index_list = []
    with open(config['DEFAULT']['QUERY_FILE'], 'r') as f:
        query_list = f.read().strip().split(',')
        query_index_list = [x for x in range(len(query_list))]
    
    
    ## Set x_guest_token per query 
    x_guest_token = AuthenticationManager.get_x_guest_token()
    

    # Create a queue to communicate with the worker threads
    queue = Queue()
    # Create 8 worker threads
    for _ in query_list:
        worker = ScrapingWorker(queue)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()

    # Put the tasks into the queue as a tuple
    for indx, row in enumerate(query_list):
        queue.put((row, x_guest_token))
        #queue.put((query, conn1, addr1, conn2, addr2))
    # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()