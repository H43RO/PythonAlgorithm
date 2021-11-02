from sys import stdin


def search(graph):
    result = 0
    # 가로로 이어지는 부분 탐색
    for i in range(n):
        length = 1
        for j in range(1, n):
            # 만약 이전 칸과 이어진다면 길이 1 증가
            if graph[i][j] == graph[i][j - 1]:
                length += 1
                continue
            result = max(result, length)
            length = 1
        result = max(result, length)  # 최댓값 갱신

    # 세로로 이어지는 부분 탐색
    for i in range(n):
        length = 1
        for j in range(1, n):
            # 만약 이전 칸과 이어진다면 길이 1 증가
            if graph[j][i] == graph[j - 1][i]:
                length += 1
                continue
            result = max(result, length)
            length = 1
        result = max(result, length)  # 최댓값 갱신

    return result


n = int(stdin.readline())
graph = [list(stdin.readline().strip()) for _ in range(n)]

max_candy = 0

for i in range(n):
    for j in range(1, n):
        # 가로로 바꿔치기 해보기
        graph[i][j], graph[i][j - 1] = graph[i][j - 1], graph[i][j]
        max_candy = max(max_candy, search(graph))
        graph[i][j], graph[i][j - 1] = graph[i][j - 1], graph[i][j]

        # 세로로 바꿔치기 해보기
        graph[j][i], graph[j - 1][i] = graph[j - 1][i], graph[j][i]
        max_candy = max(max_candy, search(graph))
        graph[j][i], graph[j - 1][i] = graph[j - 1][i], graph[j][i]

print(max_candy)
