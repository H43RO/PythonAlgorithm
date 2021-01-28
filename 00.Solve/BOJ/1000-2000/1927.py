from sys import stdin, stdout
from queue import PriorityQueue

queue = PriorityQueue()

n = int(stdin.readline())

for i in range(n):
    x = int(stdin.readline())
    if x == 0:
        if not queue.empty():
            print(queue.get())
        else:
            print(0)
    else:
        queue.put(x)
