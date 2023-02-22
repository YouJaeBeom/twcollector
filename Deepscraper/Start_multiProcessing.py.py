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
        return Falses
    def _set_daemon(self, value):
        pass
    daemon = property(_get_daemon, _set_daemon)

# We sub-class multiprocessing.pool.Pool instead of multiprocessing.Pool
# because the latter is only a wrapper function, not a proper class.
class MyPool(multiprocessing.pool.Pool):
    Process = NoDaemonProcess

# This block of code enables us to call the script from command line.
def execute(query, language, x_guest_token, conn1, addr1, conn2, addr2):
    try:
        streamscraper = ScrapingEngine.ScrapingEngine(query, language, x_guest_token, conn1, addr1, conn2, addr2)
        streamscraper.start_scraping()        
        command = "python ScrapingEngine.py --query '%s' --process_number '%s'  --x_guest_token '%s'"%(query, language, x_guest_token)
        print(command)
    except Exception as ex:
        print(ex)

def query_execute(query, conn1, addr1, conn2, addr2):
    ## language_list && language_list index list 
    with open(config['DEFAULT']['LANGUAGE_FILE'], 'r') as f:
        language_list = f.read().strip().split(',')
        language_index_list = [x for x in range(len(language_list))]
    
    ## Set x_guest_token per query 
    x_guest_token = AuthenticationManager.get_x_guest_token()

    ## langauge per process 
    process_pool = multiprocessing.Pool(processes = len(language_list))
    process_pool.starmap(execute, zip(repeat(query), language_list, repeat(x_guest_token), repeat(conn1), repeat(addr1), repeat(conn2), repeat(addr2)))
    process_pool.close()
    process_pool.join()

def tcp_connector(port):
    TCP_IP = ""
    TCP_PORT = port
    conn = None
    s = socket.socket()
    s.bind((TCP_IP, TCP_PORT))

    s.listen(1)
    print(str(port)+" listen")
    conn, addr = s.accept()
    result = []
    result.append(conn)
    result.append(addr)
    return result

    
if(__name__ == '__main__') :
    start=time.time()
    query_list =[]
    query_index_list = []

    ## query list && query index list 
    with open(config['DEFAULT']['QUERY_FILE'], 'r') as f:
        query_list = f.read().strip().split(',')
        query_index_list = [x for x in range(len(query_list))]
    

    port_list =[13000, 13001]
    ## port per process 
    process_pool = MyPool(len(port_list))
    result = process_pool.starmap(tcp_connector, zip(port_list))
    process_pool.close()
    process_pool.join()
    print(result)
    print(type(result[0]))

    conn1 = result[0][0]
    addr1 = result[0][1]
    conn2 = result[1][0]
    addr2 = result[1][1]

    ## query per process 
    process_pool = MyPool(len(query_list))
    process_pool.starmap(query_execute, zip(query_list, repeat(conn1), repeat(addr1), repeat(conn2), repeat(addr2) ))
    process_pool.close()
    process_pool.join()
    print("-------%s seconds -----"%(time.time()-start))
