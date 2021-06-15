import threading
import time

# this program is guaranteed to deadlock.
# thread 1 acquires lock1 and then after sleeping tries to acquire lock2
# but while thread 1 was sleeping, thread2 has acquired lock2
# and is trying to acquire lock1
# so thread1 is waiting (blocking) to acquire lock2
# and thread2 is waiting (blocking) to acquire lock1
# since lock1 and lock2 are never released, 

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread_1():
    print('Thread 1 starting')
    lock1.acquire()
    time.sleep(5)
    lock2.acquire()
    print('Thread 1 never gets here')

def thread_2():
    print('Thread 2 starting')
    lock2.acquire()
    time.sleep(5)
    lock1.acquire()
    print('Thread 2 never gets here')


t1 = threading.Thread(name='1',target=thread_1,args=())
t2 = threading.Thread(name='2',target=thread_2,args=())

t1.start()
t2.start()

# never gets here
