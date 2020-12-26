"""
 N X M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
 구멍이 뚫려 있는 부분끼리 상하좌우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다.
 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림 개수를 구하는 프로그램을 작성하세요.

 [입력 조건] - 첫 번째 줄에 얼음 틀의 세로 길이 N 과 가로 길이 M 이 주어집니다.
           - 두 번째 줄부터 N + 1 번째 줄까지 얼음 틀의 형태가 주어집니다.
           - 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1입니다.

 [출력 조건] - 한 번에 만들 수 있는 아이스크림 개수를 출력합니다.

 [입력 예시]     4 5
              00110
              00011
              11111
              00000

 [출력 예시]    3

"""

# DFS 를 활용한 예

n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0

# DFS 로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상하좌우 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드에 대하여 음료수 채우기
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)



