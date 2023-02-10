from multiprocessing import Process, JoinableQueue
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(queue):
    
    info('function f')
    while True:
      item = queue.get()
      if not item:
        queue.task_done()
        break
      print("processing item from process", item)
      queue.task_done()

if __name__ == '__main__':
    queue = JoinableQueue()
    process = Process(target=f, args=(queue,))
    queue.put("hello")
    queue.put("world")
    queue.put(None)
    process.start()
    process.join()
    queue.join()