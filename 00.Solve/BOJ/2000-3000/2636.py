from sys import stdin
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def print_cheese():
    for x in cheese:
        print(x)
    print()


def is_clear():
    for x in cheese:
        for c in x:
            if c == 1:
                return False
    return True


n, m = map(int, stdin.readline().split())
cheese = []

day = 0
prev_cheese = 0

for _ in range(n):
    cheese.append(list(map(int, stdin.readline().split())))

