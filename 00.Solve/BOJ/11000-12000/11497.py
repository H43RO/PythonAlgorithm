from sys import stdin
from collections import deque

T = int(stdin.readline())

for _ in range(T):
    left = deque()
    right = deque()
    n = int(stdin.readline())
    wood = list(map(int, stdin.readline().split()))

    # 입력받은 통나무 정보를 역순 정렬
    wood.sort(reverse=True)

    # pop() 하면서 차례대로 왼쪽 덱, 오른쪽 덱에 삽입
    # 격차 최소화를 위해 지그재그로 삽입하는 것이 핵심 로직
    # 예를들어 2 4 5 7 9 입력이 들어오면
    # 9 7 5 4 2 로 역순 정렬을 한 뒤
    # left = [9], right = [4, 7]
    # left = [9, 5], right = [4, 7]
    # left = [9, 5, 2], right = [4, 7]
    # 이렇게 동작하여, 각 통나무 간의 격차 최소화
    while len(wood) > 1:
        left.append(wood.pop())
        right.appendleft(wood.pop())

        if len(wood) == 1:
            left.append(wood.pop())

    # 왼쪽 덱과 오른쪽 덱 합침
    data = left + right
    # 양끝 통나무 간의 난이도 계산하여 삽입함과 동시에 list 생성
    result = [abs(data[0] - data[-1])]
    # 통나무 간의 높이 차이 (난이도) 하나씩 계산)
    for i in range(n - 1):
        result.append(abs(data[i] - data[i + 1]))

    # 그 중 가장 큰 값 출력
    print(max(result))
