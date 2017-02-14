from multiprocessing import Process, Lock

#def f(i):
def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        print('ok')
        l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()
        #Process(target=f, args=(num,)).start()

