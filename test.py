# report the default number of worker threads on your system
from concurrent.futures import ThreadPoolExecutor
# create a thread pool with the default number of worker threads
executor = ThreadPoolExecutor()
# report the number of worker threads chosen by default
print(executor._max_workers)

# SuperFastPython.com
# configure and report the default number of worker threads
from concurrent.futures import ThreadPoolExecutor
# create a thread pool with a large number of worker threads
with ThreadPoolExecutor(500) as executor:
	# report the number of worker threads
	print(executor._max_workers)


# report the number of CPUs in your system visible to Python
import os
print(os.cpu_count())
