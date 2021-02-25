from sys import stdin, stdout
from bisect import bisect_left, bisect_right


# 찾고자 하는 숫자의 가장 왼쪽 인덱스와 가장 오른쪽 인덱스의 차이가 곧 개수
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
