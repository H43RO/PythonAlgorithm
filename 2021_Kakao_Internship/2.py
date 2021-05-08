from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y):
    queue = deque()
    start_x, start_y = x, y
    queue.append((x, y))
    graph[x][y] = ('X', 0)
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if graph[nx][ny][0] == 'X':
                continue
            if graph[nx][ny][0] == 'P':
                if abs(start_x - nx) + abs(start_y - ny) <= 2:
                    if graph[x][y][1] <= 1:
                        return False
                else:
                    graph[nx][ny] = ('X', graph[x][y][1] + 1)
                    queue.append((nx, ny))

            if graph[nx][ny][0] == 'O':
                graph[nx][ny] = ('X', graph[x][y][1] + 1)
                queue.append((nx, ny))
    return True


def solution(places):
    answer = []

    for place in places:
        available = True
        # 사람이 있는 좌표 모두 저장
        people = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append((i, j))
        graph = []
        for s in place:
            temp = []
            for x in s:
                temp.append((x, 0))
            graph.append(temp)

        for person in people:
            x, y = person
            temp = copy.deepcopy(graph)
            if not bfs(temp, x, y):
                available = False
                answer.append(0)
                break
        if available:
            answer.append(1)
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
