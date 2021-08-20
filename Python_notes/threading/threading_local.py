# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:28:13 2021

@author: User
"""

import threading
import time

sleeptime = 3

# see how  _local behaves, even though it is defined outside
# thread1 and thread2 and thus is in some sense global
# there is sufficient time allowed by the time.sleep commands
# in each thread to make sure that the thread which runs second
# could overwite _local if it wanted it to. but it doesn't 
# each thread maintains its own copy of _local

# on the other hand, _global_list is declared global
# the thred which runs second will overwrite the first

_local = threading.local()
_global_list = []

def thread1():
    global _global_list
    _local.namelist = ['ambrose','walsh','mcgrath','akram']
    _global_list    = ['beatles']
    time.sleep(sleeptime)
    print(f'thread1 {_local.namelist=}')
    print(f'thread1 {_global_list=}')
    
def thread2():
    global _global_list
    _local.namelist = ['tendulkar','lara','ponting','clarke']
    _global_list    = ['dylan'] 
    time.sleep(sleeptime)
    print(f'thread2 {_local.namelist=}')
    print(f'thread2 {_global_list=}')
    

t1 = threading.Thread(target=thread1,args=())
t2 = threading.Thread(target=thread2,args=())

t1.start()
t2.start()

