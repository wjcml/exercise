import threading
import time


def job1():
    global n, lock
    with lock:
        for i in range(10):
            n += 1
            print('job1', n)
            time.sleep(2)


def job2():
    global n, lock
    with lock:
        for i in range(10):
            n += 10
            print('job2', n)
            time.sleep(1)


n = 0
# 对线程上锁，执行完该线程才执行下一条线程
lock = threading.Lock()
t1 = threading.Thread(target=job1)
t2 = threading.Thread(target=job2)
t1.start()
t2.start()