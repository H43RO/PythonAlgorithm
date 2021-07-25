from sys import stdin
from collections import deque

MAX = 100_001  # 선분 범위
n, k = map(int, stdin.readline().split())

visited = [-1] * MAX
visited[n] = 0

queue = deque([n])
while queue:
    pos = queue.popleft()
    route = [pos + 1, pos - 1, pos * 2]

    for x in route:
        # 범위를 벗어나지 않고 && (방문한 적이 없거나 || 무조건 최단거리 갱신이 가능한 경우)
        if 0 <= x < MAX and (visited[x] == -1 or visited[x] >= visited[pos] + 1):
            if x == pos * 2:  # 순간 이동의 경우
                visited[x] = visited[pos]  # 0초 후에 2 * x 위치로 이동
                queue.append(x)
                continue
            visited[x] = visited[pos] + 1  # x - 1, x + 1 로 걷는 경우 1초 소요
            queue.append(x)

print(visited[k])
