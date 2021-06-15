import threading
import time
from contextlib import contextmanager

# the whole point is to force lock acquisition in a particular order to avoid
# deadlocks. If a lock has been acquired previously, and a new thread is trying
# to acquire it, then the new thread blocks

# second, the thread local variable _local stores the locks acquired previously
# by the same thread so as to handle nested acquisitions e.g.

#def thread_2():
#    while True:
#        with acquire(y_lock):
#            with acquire(x_lock):
#                print('Thread-2')

# even, these acquisitions have to be forced to be acquired in the lock acquisition order
# decided, otherwise exception is raised


# this is thread local storage. It is NOT a global object used to communicate
# in-between threads
# otherwise, we will get into race conditions on this object.

_local = threading.local()

@contextmanager
def acquire(*locks):

    locks    = sorted(locks,key=lambda x: id(x))
    acquired = getattr(_local,'acquired',[])

    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    # acquire all of the locks
    acquired.extend(locks)

    _local.acquired = acquired
    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        for lock in reversed(locks):
            lock.release()

        del acquired[-len(locks):]
    
x_lock = threading.Lock()
y_lock = threading.Lock()

def thread_1():
    print('Entering Thread-1')
    while True:
        with acquire(x_lock,y_lock):
            print('Lock acquired Thread-1')
            time.sleep(5)
        print('Lock released Thread-1')
        break


def thread_2():
    print('Entering Thread-2')
    while True:
        with acquire(y_lock,x_lock):
            print('Lock acquired Thread-2')
            time.sleep(5)
        print('Lock released Thread-2')
        break
            
t1 = threading.Thread(target=thread_1)
t2 = threading.Thread(target=thread_2)

t1.start()
t2.start()

t1.join()
t2.join()

