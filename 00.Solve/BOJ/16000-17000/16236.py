from sys import stdin
from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


'''
    BFS 탐색을 통해 잡아먹을 수 있는 모든 물고기를 조사해보고
    그 중에서 최상단 가장 왼쪽에 있는 물고기를 잡아먹는 동작을 수행함
'''


def bfs(start_x, start_y):
    eaten = []  # 잡아먹을 수 있는 모든 물고기의 목록을 만듦
    visited = [[-1] * n for _ in range(n)]  # 최단거리를 저장할 테이블
    visited[start_x][start_y] = 0  # 시작점은 항상 최단거리 0
    queue = deque([(start_x, start_y)])
    while queue:
        x, y = queue.popleft()

        # 만약 먹을 수 있는 물고기를 만났다면 (물고기 사이즈는 항상 1 ~ 6)
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

    if not eaten:  # 먹을 수 있는 물고기 없을 경우 -1 리턴
        return -1, -1, -1
    eaten.sort(key=lambda x: (x[0], x[1], x[2]))  # 우선순위 : 최단거리에 있는 최상단 가장 왼쪽 물고기
    graph[eaten[0][1]][eaten[0][2]] = 0  # 먹은 물고기 자리는 0으로 값 바꿔줌
    return eaten[0][0], eaten[0][1], eaten[0][2]  # 먹은 물고기 최단거리, x, y 좌표 리턴


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
    distance, x, y = bfs(shark_location[0], shark_location[1])  # 일단 BFS 수행하고 보자
    if x == -1:  # 만약 먹을 수 있는 물고기가 없다면 엄마 상어 부르러 감
        break
    moved += distance  # 결과값으로 온 최단거리를 moved 에 더해줌
    shark_location = (x, y)  # 결과값으로 온 잡아먹힌 물고기 좌표를 아기 상어 좌표로 지정
    count += 1  # 물고기 잡아먹은 횟수를 1 증가
    if shark_size == count:  # 만약 아기 상어 크기만큼 물고기를 먹었다면 아기 상어 성장 및 횟수 초기화
        shark_size += 1
        count = 0

print(moved)
