from sys import stdin, stdout
from collections import deque

case = int(stdin.readline())
result = []

for i in range(case):
    n, m = map(int, stdin.readline().split())
    priority = list(map(int, stdin.readline().split()))

    queue = deque()

    for x in range(n):
        doc = list()
        doc.append(x)  # doc[0] : 인덱스
        doc.append(priority[x])  # doc[1] : 우선순위
        queue.append(doc)

    count = 0

    if len(queue) == 1:  # 만약 문서가 단 하나라면 프린트 횟수 1회로 프로그램 종료
        count += 1
        result.append(count)
        continue

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

    result.append(count)

for x in result:
    print(x)
