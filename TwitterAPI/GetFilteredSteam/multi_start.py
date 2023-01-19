import multiprocessing
from multiprocessing.pool import Pool
import time
import socket
from itertools import repeat
import time
import filtered_stream
from queue import Queue
from threading import Thread
import os


class ScrapingWorker(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        #query, language, x_guest_token, conn, addr = self.queue.get()
        # index, query, api, conn, addr = self.queue.get()
        index, query, api = self.queue.get()
        try:
            # stream = filtered_stream.Filtered_stream(index, query, api, conn, addr)
            stream = filtered_stream.Filtered_stream(index, query, api)
            stream.main()
        except Exception as ex:
            print(ex)      
        
        self.queue.task_done()


if __name__ == '__main__' :
    """## Kafka & Spark
    TCP_IP = "117.17.189.206"
    TCP_PORT = 13000
    conn = None
    s = socket.socket()
    s.bind((TCP_IP, TCP_PORT))

    s.listen(1)
    print("Lelay engine waiting")
    conn, addr = s.accept()"""

    queue_list = [
        ['russia', '%3DKXeGiIQQmpb8YgtfGGT71bq89NnYmEtmMGHMkMrt1ObabPCeDE'],
        ['Ukraine', '%3D909d1u2PncGrJ8OHyYp4u3W7pZxxycB6tXzAnkyOXqn54uzHG0'],
        ['Putin', '%2Bvq4KHg%3DG7ycYpX4ploINxCb8pV7WcJsjOxmOQgEML5taUihHaevet3hSo'],
        ['war', '%3Dg11NtzKL58hE2uwVMvwNk6JYIED5mjwzcOXH7pN9WhEcGy58Di'],
        ['russian','%3DPC703Bn71ETZOGa3OJoxrCEXvMDyDH4jL13845n2d7JHoZDVkm'],
        ['bts', '%3DKXeGiIQQmpb8YgtfGGT71bq89NnYmEtmMGHMkMrt1ObabPCeDE'],
        ['@BTS_twt', '%3D909d1u2PncGrJ8OHyYp4u3W7pZxxycB6tXzAnkyOXqn54uzHG0'],
        ['#bts', '%2Bvq4KHg%3DG7ycYpX4ploINxCb8pV7WcJsjOxmOQgEML5taUihHaevet3hSo'],
        ['jimin', '%3Dg11NtzKL58hE2uwVMvwNk6JYIED5mjwzcOXH7pN9WhEcGy58Di'],
        ['RM','%3DPC703Bn71ETZOGa3OJoxrCEXvMDyDH4jL13845n2d7JHoZDVkm']
    ]

    tweetIDfile = 'tweetID/tweetID.txt'
    if os.path.exists(tweetIDfile ):
        os.remove(tweetIDfile)
        print("The file has been deleted successfully")
    else:
        print("The file does not exist!")
        os.makedirs(os.path.dirname(tweetIDfile), exist_ok=True)

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
        #queue.put(( indx, row[0], row[1], conn, addr))
        queue.put(( indx, row[0], row[1]))
        #queue.put((query, conn1, addr1, conn2, addr2))
    # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()
