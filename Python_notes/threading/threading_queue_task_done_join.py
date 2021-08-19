# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 12:51:28 2021

@author: User
"""

from queue import Queue
from threading import Thread
import time,random

# the point of the q.join() is to block until all the data has
# been processed by the consumer.
# this is done by keeping a track of how many items are put in the queue
# 
# if the time.sleep in consumer are removed
# the join doesn't work because either
#   1) by the time the code gets to q.join()
#      the number of items put into the queue and processed are equal

def producer(out_q):
    data_list = ['john','paul','george','ringo','shutdown']
    for data in data_list:
        print('producer putting data=',data)                             
        out_q.put(data)
        
def consumer(in_q):
   # time.sleep(4)
    while True:
        data = in_q.get()
        print('consumer got ',data)
        in_q.task_done()
        # time.sleep(2)
        if (data == 'shutdown'):
            break
        
    print('Terminating consumer')


q  = Queue()

t1 = Thread(target=consumer,args=(q,))
t2 = Thread(target=producer,args=(q,))

t1.start()
t2.start()


q.join()    

print('-'*80)
print('after queue join')
print('-'*80)