from queue import Queue
from threading import Thread
import time

# the queue data structure is threadsafe
# in the following example, the producer puts data into the queue
# waits (out_q.join()) to see if the task has been done
# before putting new items into the queue

# if a consumer thread calls task_done on the queue,
# then the producer thread moves past the join


def producer(out_q):
    data = [0,1,2,3,4,5,6,7,8,9]
    while data:
        out_q.put(data.pop(0))
        out_q.join()
        print('Got task_done in producer')


def consumer(name,in_q):
    while True:
        data = in_q.get()
        print(f'Thread {name=} got {data=}')
        time.sleep(2)
        in_q.task_done()
        if (data == 9):
            print(f'Thread {name} shutting down ')
            in_q.put(data)
            break
        
q  = Queue()
t1 = Thread(target=consumer,args=(0,q))
t2 = Thread(target=consumer,args=(1,q))
t3 = Thread(target=producer,args=(q,))
t1.start()
t2.start()
t3.start()
