import sys

sys.setrecursionlimit(10000)  # 재귀 깊이 제한을 풀어줘야 정답 처리


def dfs(graph, x, y):
    # 농장 범위 밖을 나가게 되면 False 반환
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 해당 좌표에 배추가 심어져있다면
    if graph[x][y] == 1:
        # 탐색했으므로 0 으로 바꿔줌
        graph[x][y] = 0
        # 상하좌우 네 방향에 대하여 DFS 탐색 시작
        dfs(graph, x - 1, y)
        dfs(graph, x, y - 1)
        dfs(graph, x + 1, y)
        dfs(graph, x, y + 1)
        return True
    return False


case = int(input())
result = [0] * case

for i in range(case):
    # 농장의 세로 길이, 가로 길이, 배추 개수 입력
    n, m, k = map(int, input().split())
    # 농장 정보를 담을 그래프 선언
    graph = [[0] * m for _ in range(n)]
    for x in range(k):
        # 배추가 심어진 좌표에 1 입력
        a, b = map(int, input().split())
        graph[a][b] = 1
    # 모든 좌표에 대하여 DFS 탐색
    for x in range(n):
        for y in range(m):
            # 만약 True 를 반환했다면 (인접 배추 모두 탐색 완료)
            if dfs(graph, x, y):
                # 결과 1 증가
                result[i] += 1

for x in result:
    print(x)
