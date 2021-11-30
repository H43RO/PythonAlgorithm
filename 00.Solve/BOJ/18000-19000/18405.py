from sys import stdin
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    count = 0
    while queue:
        if count == count_max:  # 입력으로 주어진 초 도달하면 탐색 종료
            break
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y]  # 바이러스 번호 그대로 전파
                    queue.append((nx, ny))
        count += 1  # 초 세기

    return graph[virus_x - 1][virus_y - 1]  # 입력으로 주어진 (x, y) 값 반환


n, k = map(int, stdin.readline().split())

graph = []
virus = []

for i in range(n):
    temp = list(map(int, stdin.readline().split()))
    for j in range(n):
        if temp[j] != 0:
            virus.append((temp[j], i, j))  # 바이러스의 번호, 좌표 저장
    graph.append(temp)

queue = deque([])
for num, x, y in sorted(virus):  # 바이러스 우선순위대로 정렬 (바이러스 번호 기준)
    queue.append((x, y))

count_max, virus_x, virus_y = map(int, stdin.readline().split())

print(bfs())
