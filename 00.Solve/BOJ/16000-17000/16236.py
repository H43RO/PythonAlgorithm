from sys import stdin
from collections import deque

dx = [0, -1, 0, 1]  # 차례대로 윗쪽, 왼쪽을
dy = [1, 0, -1, 0]  # 우선으로 탐색하도록 함


# BFS 한 번 수행한다는 것은  무조건 물고기를 1마리 먹는 뜻임
def bfs(start_x, start_y):
    graph[start_x][start_y] = 0
    eaten = []
    visited = [[-1] * n for _ in range(n)]
    visited[start_x][start_y] = 0
    queue = deque([(start_x, start_y)])
    while queue:
        x, y = queue.popleft()

        # 만약 먹을 수 있는 물고기를 만났다면
        if graph[x][y] in range(1, 7) and graph[x][y] < shark_size:
            eaten.append((visited[x][y], x, y))

        # 4가지 이동 방향에 대하여
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 넘지 않고 방문한 적 없으며, 아기 상어 몸집보다 더 큰 개체가 없을 경우 (크기 같으면 지나갈 순 있음)
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and graph[nx][ny] <= shark_size:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    if not eaten:
        return -1, -1, -1
    eaten.sort(key=lambda x: (x[0], x[1], x[2]))
    graph[eaten[0][1]][eaten[0][2]] = 0
    return eaten[0][0], eaten[0][1], eaten[0][2]


n = int(stdin.readline())
graph = []
shark_location = (0, 0)  # 상어의 좌표를 담을 변수

for i in range(n):
    line = list(map(int, stdin.readline().split()))
    graph.append(line)
    if 9 in line:
        shark_location = (i, line.index(9))

moved = 0  # 아기 상어가 엄마를 부르기까지 얼마나 움직였는지
shark_size = 2  # 초기 아기 상어 크기는 2
count = 0  # shark 값과 같아지면 shark 를 1 늘리고 eaten 0 으로 초기화  (eaten 은 BFS 수행 시 마다 무조건 1씩 늘어남)

while True:
    # 먹을 수 있는 물고기가 있다면 BFS 를 수행하자!
    distance, x, y = bfs(shark_location[0], shark_location[1])
    if x == -1:
        break
    moved += distance
    shark_location = (x, y)
    count += 1
    if shark_size == count:
        shark_size += 1
        count = 0

print(moved)
