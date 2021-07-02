from sys import stdin
import heapq

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dijkstra():  # 무조건 (0, 0) 시작이므로 시작점 입력 안 받아도 됨
    q = []
    heapq.heappush(q, (0, (0, 0)))  # 지금까지 벽 부순 횟수, (x, y) 좌표를 통해 다익스트라 수행 (벽 부순 횟수를 가중치로)
    destroyed[0][0] = 0  # 시작점은 항상 뚫려있음 -> 벽 부순 횟수 0
    while q:
        count, (x, y) = heapq.heappop(q)  # 힙 내에서 벽 부순 횟수가 가장 적은 (x, y) 좌표 꺼냄
        destroyed[x][y] = count  # 해당 좌표까지의 벽 부순 횟수인 count 를 저장함
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and destroyed[nx][ny] < 0:  # 미로 범위를 넘지 않고 한 번도 방문한 적 없다면
                if graph[nx][ny] == 1:  # 만약 벽을 만났다면
                    heapq.heappush(q, (count + 1, (nx, ny)))  # 벽 부순 횟수를 1 증가하여 다익스트라 큐에 큐잉
                else:
                    heapq.heappush(q, (count, (nx, ny)))  # 아니라면 벽 부순 횟수를 그대로 두고 다익스트라 큐에 큐잉


m, n = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().strip())) for _ in range(n)]
destroyed = [[-1] * m for _ in range(n)]
dijkstra()  # 다익스트라 수행

print(destroyed[n - 1][m - 1])
