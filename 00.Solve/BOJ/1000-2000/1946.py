from sys import stdin, stdout
from collections import deque

case = int(stdin.readline().strip())
results = []
for _ in range(case):
    n = int(stdin.readline().strip())

    people = deque()
    for i in range(n):
        people.append(tuple(map(int, stdin.readline().split())))
    people = deque(sorted(people))
    interview_min = people[0][1]
    people.popleft()
    count = 1
    # 순위는 낮을 수록 좋은 것
    # 매번 가장 우수한 사람과 교차 비교하여 둘 중 하나라도 우수하면 (값이 더 작으면) 합격
    for x in people:
        if interview_min > x[1]:
            count += 1
            interview_min = x[1]
        else:
            continue
    results.append(count)

for x in results:
    print(x)
