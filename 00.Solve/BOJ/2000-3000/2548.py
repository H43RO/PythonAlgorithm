"""
중앙값 이용한 풀이, 브루트포스 이용한 풀이
"""
import sys
from sys import stdin


def median_solve():
    """
    중앙값 이용한 풀이
    """
    print(data[n // 2 - 1])
    exit()


def bp_solve():
    """
    브루트포스 이용한 풀이
    """
    min_result = (sys.maxsize, 0)
    for x in data:
        temp = 0
        for a in data:
            temp += abs(x - a)
        min_result = min(min_result, (temp, x))
    print(min_result[1])
    exit()


n = int(stdin.readline())
# data = sorted(list(map(int, stdin.readline().split())))  # 중앙값으로 풀 때
data = list(map(int, stdin.readline().split()))  # 브루트포스로 풀 때

bp_solve()
