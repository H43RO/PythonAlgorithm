from sys import stdin, stdout
from collections import deque

case = int(stdin.readline())

for i in range(case):
    n, m = map(int, stdin.readline().split())
    priority = list(map(int, stdin.readline().split()))

    queue = deque()  # 프린터 큐 생성
    for x in range(n):
        doc = [x, priority[x]]  # [0] : 인덱스, [1] : 우선순위
        queue.append(doc)  # 프린터 큐에 큐잉

    count = 0
    while queue:
        doc = queue[0]  # 현재 큐의 맨 앞 문서
        max_doc = max(queue, key=lambda item: item[1])  # 우선순위가 가장 높은 문서

        if doc[1] != max_doc[1]:  # 현재 큐의 맨 앞 문서의 우선순위가 최고순위가 아니라면
            queue.append(queue.popleft())  # 큐 맨 뒤로 이동

        if doc[1] == max_doc[1]:  # 현재 맨 앞 문서의 우선순위가 최고순위라면
            queue.popleft()  # 큐에서 제거 후
            count += 1  # 프린트 횟수 1 증가
            if doc[0] == m:  # 만약 타겟 문서라면 종료
                break

    print(count)
