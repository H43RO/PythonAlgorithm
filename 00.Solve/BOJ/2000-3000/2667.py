n = int(input())

# 지도 정보
graph = []

# 총 단지 수
result = 0

# 각 단지 내 집의 수를 저장하는 리스트
counts = []
# 각 단지 내 집의 수
count = 0

for i in range(n):
    graph.append(list(map(int, input())))


def dfs_function(x, y):
    global count
    # 지도 밖으로 나가는 경우 False 리턴
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 해당 좌표가 집일 경우
    if graph[x][y] == 1:
        # count 증가
        count += 1
        # 이미 탐색했으므로 값 0 으로 변경
        graph[x][y] = 0
        # 상하좌우 방향에 대하여 DFS 탐색 시작
        dfs_function(x - 1, y)
        dfs_function(x + 1, y)
        dfs_function(x, y - 1)
        dfs_function(x, y + 1)
        return True
    return False

# 모든 좌표에 대하여 DFS 탐색 시도
for i in range(n):
    for j in range(n):
        # DFS 결과가 True 라면 (해당 단지가 모두 탐색된 상태)
        if dfs_function(i, j) == True:
            # 단지 수 1 증가
            result += 1
            # 단지 내 집의 수 증가하고 저장한 뒤 초기화
            counts.append(count)
            count = 0


print(result)

counts.sort()
for x in counts:
    print(x)
