import logging
import time
import concurrent.futures
import threading

# https://realpython.com/intro-to-python-threading/#what-is-a-thread
class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self,name):
        logging.info(f'Thread {name}: starting update')
        logging.info(f'Thread {name}: releasing lock')
        
        # If you try to release a lock which has not been acquired
        # a RuntimeError is raised which is silently trapped by
        # ThreadPoolExecutor context manager
        # so is the following maunally raised RuntimeError
        # raise RuntimeError(f'RT Error Thread {name}')
        # self._lock.release()
        
        logging.info(f'Thread {name}: released lock')
        
        with self._lock:
            logging.info(f'Thread {name} has lock')
            local_copy  = self.value
            local_copy += 1
            time.sleep(1)
            self.value = local_copy
            logging.info(f'Thread {name} about to release lock')
            
        logging.info(f'Thread {name}')
        logging.info(f'Thread {name}: finishing update')

if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format,level=logging.INFO,datefmt='%H:%M:%S')
    database = FakeDatabase()
    logging.info(f'Testing update. Starting value is {database.value}')
    nthreads = 2
    with concurrent.futures.ThreadPoolExecutor(max_workers=nthreads) as executor:
        for index in range(nthreads):
            executor.submit(database.update,index)

    logging.info(f'Testing update. Ending value is {database.value}')
    


        
