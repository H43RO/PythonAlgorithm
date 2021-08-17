from sys import stdin

"""
'꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는...' 이라고 하길래
그냥 점 1개도 크기 1 짜리 정사각형으로 치는지 전혀 몰랐다.
"""


def search_square():
    """
    변의 길이를 최대에서 1씩 줄여가며, 탐색 가능한 범위 내에서 꼭짓점 4 좌표를 모두 검사
    :return:    꼭짓점에 쓰여있는 수가 모두 같은 가장 큰 정사각형의 '변'의 길이
    """
    global standard
    while standard:
        for i in range(n - standard):
            for j in range(m - standard):
                if graph[i][j] == graph[i][j + standard] == graph[i + standard][j] == graph[i + standard][j + standard]:
                    return standard + 1  # 사전에 임의로 -1 을 해준 값이므로, 1을 더하여 리턴
        standard -= 1
    return 1  # 위 루프 내에서 리턴이 일어나지 않았다면, 크기가 1인 정사각형이 최댓값임


n, m = map(int, stdin.readline().split())
graph = [list(stdin.readline().strip()) for _ in range(n)]
standard = min(n, m) - 1  # 최대 변의 길이 저장 (매끄러운 루프 순회를 위해 -1 해줌)

print(search_square() ** 2)  # 면적 출력
