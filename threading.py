#! /usr/bin/python
import threading
import time

def worker():
    print (threading.currentThread().getName(),'Lanzado')
    time.sleep(2)
    print (threading.currentThread().getName(),'Detenido')
