"""
 N X M 크기의 정사각형 형태의 미로에 갇혔습니다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 합니다.
 동빈이의 위치는 (1, 1) 이며, 미로의 출구는 (N, M) 위치에 존재하며 한 번에 한 칸씩 이동할 수 있습니다.
 이때 괴물이 있는 부분은 0 으로, 없는 부분은 1 로 표시되어 있습니다. 미로는 반드시 탈출할 수 있는 형태로 제시됩니다.
 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산합니다.

 [입력 조건]  첫째 줄에 두 정수 N, M 이 주어집니다. 다음 N 개의 줄에는 각각 M 개의 정수로 미로의 정보가 주어집니다.
            각각의 수들은 공백 없이 붙어서 입력으로 제시됩니다. 또한 시작 칸과 마지막 칸은 항상 1입니다.

 [출력 조건] - 첫째 줄에 최소 이동칸의 개수를 출력합니다.

 [입력 예시]     5 6
              101010
              111111
              000001
              111111
              111111

 [출력 예시]    10

"""

# BFS 는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색함
# 따라서 (1, 1) 지점부터 BFS 를 수행하여 모든 노드의 최단 거리 값을 기록하면 해결할 수 있음

from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 시작점으로부터 BFS 를 수행하면서 상하좌우 모든 노드에 대하여 이동 간선 길이 (비용) 을 기록
# 그러므로 BFS 를 수행하고나면 마지막 노드에 적혀있는 이동 간선 길이가 곧 최소 이동칸 개수임

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물이 있는 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]


print(bfs(0, 0))