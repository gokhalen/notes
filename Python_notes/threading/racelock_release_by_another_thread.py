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
        logging.info(f'Thread {name}: about to lock')

        # attempt to release the lock if it has been acquired by someone else
        # so we are releasing a lock acquired by another thread - dangerous it is
        # answer will always be 1, instead of 2
        # this is one reason Rlock is better (but slower)

        try:
            self._lock.release()
            self._lock.acquire()
        except:
            self._lock.acquire()
            
        logging.debug(f'Thread {name} has lock')
        local_copy  = self.value
        local_copy += 1
        time.sleep(0.2)
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
    


        
