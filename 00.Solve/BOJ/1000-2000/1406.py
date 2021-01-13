from collections import deque
from sys import stdin, stdout

# List 형태로 단순히 인덱스를 커서로 삼아 삽입, 삭제를 하다보면
# 배열 순서 정렬 과정이 오래 걸려 시간 초과 판정을 받게 됨
# 배열 중간에서 어떤 연산이 일어나든 시간이 오래 걸린다는 것이 포인트

# 다만 배열의 맨 앞과 맨 뒤의 추가 및 삭제는 메모리의 할당과 삭제뿐이므로
# 연산 시간 복잡도가 상수 시간 O(1) 임
# 따라서 항상 배열의 끝에서만 연산이 일어날 수 있도록 생각해봄

# 핵심 아이디어 : 커서를 기준으로 왼쪽, 오른쪽 덱으로 쪼개어 문제 구현

init = list(stdin.readline().strip())
m = int(stdin.readline())

# 초기 문자열은 Left 덱에 저장
left = deque(init)
right = deque()

for i in range(m):
    command = stdin.readline().split()

    # Left 덱이 비어있지 않고 L 명령어가 들어왔을 때
    if command[0] == 'L' and left:
        # Left 덱의 가장 오른쪽 문자를 Right 덱의 맨 앞에 삽입
        right.appendleft(left.pop())

    # Right 덱이 비어있지 않고 D 명령어가 들어왔을 때
    if command[0] == 'D' and right:
        # Right 덱의 가장 왼쪽 문자를 Left 덱의 맨 뒤에 삽입
        left.append(right.popleft())

    # Left 덱이 비어있지 않고 B 명령어가 들어왔을 때
    if command[0] == 'B' and left:
        # Left 덱의 가장 오른쪽 문자 삭제
        left.pop()

    # P 명령어가 들어왔을 때
    if command[0] == 'P':
        # Left 덱의 가장 오른쪽에 입력된 문자 삽입
        left.append(str(command[1]))

# Left 덱과 Right 덱을 합친 결과가 Result
result = left + right

for x in result:
    print(x, end="")
