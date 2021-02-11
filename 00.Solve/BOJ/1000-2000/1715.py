from sys import stdin, stdout
from queue import PriorityQueue

n = int(stdin.readline().strip())
num = PriorityQueue()

for _ in range(n):
    num.put(int(stdin.readline().strip()))

if num.qsize() == 1:
    print(0)
elif num.qsize() == 2:
    print(num.get() + num.get())
else:
    result = 0

    while num.qsize() > 1:
        temp = num.get() + num.get()
        result += temp

        if num.qsize() == 0:
            break
        else:
            num.put(temp)

    print(result)
