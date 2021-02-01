import multiprocessing


def thread_func():
    while True:
        pass


if __name__ == "__main__":
    cpus = 7
    t = []
    for i in range(0, cpus):
        thread = multiprocessing.Process(target=thread_func)
        thread.start()
        t.append(thread)
    print('Heating up the CPU...')
    for i in range(0, cpus):
        t[i].join()
