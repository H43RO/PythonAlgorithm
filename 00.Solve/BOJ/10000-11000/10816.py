from sys import stdin, stdout
from bisect import bisect_left, bisect_right


def count(n, left_value, right_value):
    right_index = bisect_right(n, right_value)
    left_index = bisect_left(n, left_value)

    return right_index - left_index


n = int(stdin.readline())
card = list(map(int, stdin.readline().split()))

m = int(stdin.readline())
want = list(map(int, stdin.readline().split()))

card.sort()

for x in want:
    print(count(card, x, x), end=" ")
