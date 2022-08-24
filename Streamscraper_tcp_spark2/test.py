import socket
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

class NoDaemonProcess(multiprocessing.Process):
    # make 'daemon' attribute always return False
    def _get_daemon(self):
        return False
    def _set_daemon(self, value):
        pass
    daemon = property(_get_daemon, _set_daemon)

# We sub-class multiprocessing.pool.Pool instead of multiprocessing.Pool
# because the latter is only a wrapper function, not a proper class.
class MyPool(multiprocessing.pool.Pool):
    Process = NoDaemonProcess


def query_execute(query):
    while(1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.connect(('117.17.189.206', 13000))     # 접속할 서버의 ip주소와 포트번호를 입력.
        sock.send(query.encode())                 # 내가 전송할 데이터를 보냄.

if(__name__ == '__main__') :
    start=time.time()
    query_list =[]
    query_index_list = []

    ## query list && query index list 
    with open(config['DEFAULT']['QUERY_FILE'], 'r') as f:
        query_list = f.read().strip().split(',')
        query_index_list = [x for x in range(len(query_list))]
    

    ## query per process 
    process_pool = MyPool(len(query_list))
    process_pool.map(query_execute, (query_list))
    process_pool.close()
    process_pool.join()
    print("-------%s seconds -----"%(time.time()-start))
