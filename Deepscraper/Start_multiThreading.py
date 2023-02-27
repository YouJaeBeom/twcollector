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
        port_list = [x for x in range(10000,10200)]
        #port = random.randint(10000,10200)
        index, query, language, x_guest_token, conn, addr = self.queue.get()

        streamscraper = ScrapingEngine.ScrapingEngine(query, port_list[index], language, x_guest_token, conn, addr)
        streamscraper.start_scraping()        
        self.queue.task_done()


if __name__ == '__main__':
    start=time.time()

    query_list =[]
    query_index_list = []
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
    
    
    ## Set x_guest_token per query 
    x_guest_token = AuthenticationManager.get_x_guest_token()

<<<<<<< HEAD
    send_mode = config['DEFAULT']['SEND_MODE']

    if send_mode == "tcp":
        TCP_IP = "117.17.189.206"
        TCP_PORT = 13000
        conn = None
        s = socket.socket()
        s.bind((TCP_IP, TCP_PORT))

        s.listen(1)
        print("Lelay engine waiting")
        conn, addr = s.accept()
        # Create a queue to communicate with the worker threads
        queue = Queue()
        # Create 8 worker threads
        for _ in queue_list:
            worker = ScrapingWorker(queue)
            # Setting daemon to True will let the main thread exit even though the workers are blocking
            worker.daemon = True
            worker.start()

        # Put the tasks into the queue as a tuple
        for indx, row in enumerate(queue_list):
            queue.put(( indx, row[0], row[1], x_guest_token, conn, addr))
            #queue.put((query, conn1, addr1, conn2, addr2))
        # Causes the main thread to wait for the queue to finish processing all the tasks
        queue.join()
    else:
        conn, addr = None, None
        # Create a queue to communicate with the worker threads
        queue = Queue()
        # Create 8 worker threads
        for _ in queue_list:
            worker = ScrapingWorker(queue)
            # Setting daemon to True will let the main thread exit even though the workers are blocking
            worker.daemon = True
            worker.start()

        # Put the tasks into the queue as a tuple
        for indx, row in enumerate(queue_list):
            queue.put(( indx, row[0], row[1], x_guest_token, conn, addr))
            #queue.put((query, conn1, addr1, conn2, addr2))
        # Causes the main thread to wait for the queue to finish processing all the tasks
        queue.join()
=======
    TCP_IP = ""
    TCP_PORT = 
    conn = None
    s = socket.socket()
    s.bind((TCP_IP, TCP_PORT))

    s.listen(1)
    print("Lelay engine waiting")
    conn, addr = s.accept()
    
    

    # Create a queue to communicate with the worker threads
    queue = Queue()
    # Create 8 worker threads
    for _ in queue_list:
        worker = ScrapingWorker(queue)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()

    # Put the tasks into the queue as a tuple
    for indx, row in enumerate(queue_list):
        queue.put(( indx, row[0], row[1], x_guest_token, conn, addr))
        #queue.put((query, conn1, addr1, conn2, addr2))
    # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()
>>>>>>> 2a2fc918ccbeaf7c9a6cf343fb474e708939727e
    
