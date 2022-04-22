import multiprocessing
import os


def thread_func():
    while True:
        pass


if __name__ == "__main__":
    cpus = os.cpu_count()
    t = []
    for i in range(0, cpus):
        thread = multiprocessing.Process(target=thread_func)
        thread.start()
        t.append(thread)
    print('Heating up the CPU...')
    for i in range(0, cpus):
        t[i].join()
