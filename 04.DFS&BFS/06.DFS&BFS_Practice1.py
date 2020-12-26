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

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)



