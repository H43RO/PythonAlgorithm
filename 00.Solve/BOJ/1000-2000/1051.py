from sys import stdin

'''
    '꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는...' 이라고 하길래
    그냥 점 1개도 크기 1 짜리 정사각형으로 치는지 전혀 몰랐다.
'''


def search_square():
    global standard
    while standard:
        for i in range(n - standard):
            for j in range(m - standard):
                if graph[i][j] == graph[i][j + standard] == graph[i + standard][j] == graph[i + standard][j + standard]:
                    return standard
        standard -= 1
    return 0


n, m = map(int, stdin.readline().split())
graph = [list(stdin.readline().strip()) for _ in range(n)]
standard = min(n, m) - 1  # 측정 기준 줄여가면서 탐색

print((search_square() + 1) ** 2)
