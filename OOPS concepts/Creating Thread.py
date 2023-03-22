import _thread
import time
def display(val):
    i=0
    while i<5:
        i=i+1
        time.sleep(2)
        print('Display function')
def printing(val):
    i=0
    while i<5:
        i=i+1
        time.sleep(1)
        print('printing function')
try:
    _thread.start_new_thread(display,('thread1',))
    _thread.start_new_thread(printing,('thread1',))
except:
    print('thread not started....error')