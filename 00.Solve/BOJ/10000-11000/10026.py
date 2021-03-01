from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, target, graph):
    if 0 <= x < n and 0 <= y < n:
        if graph[x][y] == 'X' or graph[x][y] != target:
            return False
        # 방문한 곳으로 표시
        graph[x][y] = 'X'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            dfs(nx, ny, target, graph)
        return True
    return False


normal_graph = []
weakness_graph = []

normal_count = {'R': 0, 'G': 0, 'B': 0}
weakness_count = {'R': 0, 'B': 0}

n = int(stdin.readline())

for _ in range(n):
    # 값 변형이 같이 따라가기 때문에 copy() 를 통해 생성
    temp1 = list(stdin.readline().strip())
    temp2 = temp1.copy()
    normal_graph.append(temp1)
    for i in range(n):
        if temp2[i] == 'G':
            temp2[i] = 'R'
    weakness_graph.append(temp2)

for i in range(n):
    for j in range(n):
        if normal_graph[i][j] != 'X':
            normal_count[normal_graph[i][j]] += 1
            dfs(i, j, normal_graph[i][j], normal_graph)

for i in range(n):
    for j in range(n):
        if weakness_graph[i][j] != 'X':
            weakness_count[weakness_graph[i][j]] += 1
            dfs(i, j, weakness_graph[i][j], weakness_graph)

print(normal_count['R'] + normal_count['G'] + normal_count['B'], end=' ')
print(weakness_count['R'] + weakness_count['B'])
