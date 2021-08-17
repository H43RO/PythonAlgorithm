from sys import stdin, setrecursionlimit

setrecursionlimit(1000000000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, number):
    """
    DFS 탐색을 수행하는 함수
    :param x:      탐색을 시작하는 위치의 X 좌표
    :param y:      탐색을 시작하는 위치의 Y 좌표
    :param number: 한 글자씩 이어지는 숫자를 담는 변수  e.g. "1122" -> "11221"
    :return:       number 의 길이가 6이 되면 재귀 종료
    """
    if len(number) == 6:  # 숫자 길이가 6이 되었다면
        if number not in result:  # 중복체크 통과 시 result 에 추가
            result.append(number)
        return  # 재귀 종료

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:  # 그래프 범위 내 일때
            dfs(nx, ny, number + graph[nx][ny])  # 탐색한 숫자를 뒤에 덧붙임


result = []  # 가능한 모든 경우의 수를 담는 리스트
graph = [list(map(str, stdin.readline().split())) for _ in range(5)]

for i in range(5):  # 만들 수 있는 모든 경우를 순회
    for j in range(5):
        dfs(i, j, graph[i][j])

print(len(result))
