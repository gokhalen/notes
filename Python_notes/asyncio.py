# https://towardsdatascience.com/introduction-to-asynchronous-programming-in-python-3cd190748cd5
# https://stackoverflow.com/questions/27435284/multiprocessing-vs-multithreading-vs-asyncio-in-python-3

'''
if io_bound:
    if io_very_slow:
        print("Use Asyncio")
    else:
        print("Use Threads")
else:
    print("Multi Processing")
'''

'''
asyncio is essentially threading where not the CPU but you, as a programmer (or actually your application), decide where and when does the context switch happen. In Python you use an await keyword to suspend the execution of your coroutine (defined using async keyword).
'''
