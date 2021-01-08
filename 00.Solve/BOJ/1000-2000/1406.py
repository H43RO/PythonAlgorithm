from collections import deque
from sys import stdin, stdout

# List 형태로 단순히 삽입, 삭제를 하다보면
# 배열 순서 정렬 과정이 오래 걸려 시간 초과 판정을 받게 됨

# 커서를 기준으로 왼쪽, 오른쪽 덱으로 쪼개어 생각해봄

init = list(stdin.readline().strip())
m = int(stdin.readline())

left = deque(init)
right = deque()

for i in range(m):
    command = stdin.readline().split()
    if command[0] == 'L' and left:
        right.appendleft(left.pop())
    if command[0] == 'D':
        if right:
            left.append(right.popleft())
    if command[0] == 'B':
        if left:
            left.pop()
    if command[0] == 'P':
        left.append(str(command[1]))

result = left + right

for x in result:
    print(x, end="")
