import time
from threading import Thread


# 自定义线程函数。
def main(name="Python"):
    for i in range(2):
        print("hello", name)
        time.sleep(1)


# 创建线程01，不指定参数
thread_01 = Thread(target=main)
# 启动线程01
thread_01.start()


# 创建线程02，指定参数，注意逗号
thread_02 = Thread(target=main, args=("MING",))
# 启动线程02
thread_02.start()