from sys import stdin, stdout
from queue import PriorityQueue

n = int(stdin.readline())

lectures = []
classes = PriorityQueue()

for i in range(n):
    lectures.append(list(map(int, stdin.readline().split())))

lectures.sort(key=lambda x: x[0])

# 맨 처음 강의의 끝나는 시간을 우선순위 큐에 삽입
classes.put(lectures[0][1])

for i in range(1, n):
    # 강의 시작 시간이 제일 먼저 끝나는 강의의 끝나는 시간 이후라면
    # 제일 먼저 끝나는 강의와 (우선순위 큐의 최상위) 바꿔치기
    if classes.queue[0] <= lectures[i][0]:
        classes.get()
        classes.put(lectures[i][1])
    # 해당 사항이 없다면 우선순위 큐에 그대로 넣어줌
    else:
        classes.put(lectures[i][1])

print(classes.qsize())
