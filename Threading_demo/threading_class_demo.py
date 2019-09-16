import time
from threading import Thread
import threading


class MyThread(Thread):
    def __init__(self, name="Python"):
        # 注意，super().__init__() 一定要写
        # 而且要写在最前面，否则会报错。
        super().__init__()
        self.name = name

    def run(self):
        for i in range(2):
            print("hello", self.name)
            time.sleep(1)


if __name__ == '__main__':
    # 创建线程01，不指定参数
    thread_01 = MyThread()
    # 创建线程02，指定参数
    thread_02 = MyThread("MING")

    thread_01.start()
    # 阻塞线程，执行完阻塞线程才能执行下一条线程
    # thread_01.join()

    thread_02.start()

