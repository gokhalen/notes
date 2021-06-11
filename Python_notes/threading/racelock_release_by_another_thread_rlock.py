import logging
import time
import concurrent.futures
import threading

# https://realpython.com/intro-to-python-threading/#what-is-a-thread
# https://stackoverflow.com/questions/22885775/what-is-the-difference-between-lock-and-rlock
class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.RLock()

    def update(self,name):
        logging.info(f'Thread {name}: starting update')
        logging.info(f'Thread {name}: about to lock')

        # attempt to release the RLock if it has been acquired by someone else
        # so we are releasing a RLock acquired by another thread
        # unlike Lock, we cannot release a RLock acquired by another thread
        # this is one reason Rlock is better (but slower)

        try:
            logging.info(f'Thread {name} trying to steal lock')
            self._lock.release()
            self._lock.acquire()
        except:
            logging.info(f'Exception raised, thread {name} now waiting for acquire')
            self._lock.acquire()
            logging.info(f'Thread {name} has acquired lock')
            
        logging.debug(f'Thread {name} has lock')
        local_copy  = self.value
        local_copy += 1
        time.sleep(2)
        self.value = local_copy
        logging.debug(f'Thread {name} about to release lock')
        self._lock.release()
        
            
        logging.info(f'Thread {name}')
        logging.info(f'Thread {name}: finishing update')

if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format,level=logging.INFO,datefmt='%H:%M:%S')
    database = FakeDatabase()
    logging.info(f'Testing update. Starting value is {database.value}')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update,index)

    logging.info(f'Testing update. Ending value is {database.value}')
    


        
