from sys import stdin, stdout
from collections import deque


def bfs(M, N, box):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    days = -1

    # 익은 토마토를 다 처리할 때 까지
    while ripe:
        days += 1
        # 익은 토마토를 하나씩 pop()
        for _ in range(len(ripe)):
            x, y = ripe.popleft()

            # 상하좌우 네 가지 방향에 대하여 탐색 기록 해줌
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (0 <= nx < N) and (0 <= ny < M) and (box[nx][ny] == 0):
                    box[nx][ny] = box[x][y] + 1
                    # 탐색하면 해당 토마토도 익었다는 뜻이므로 익은 토마토 목록에 추가해줌
                    ripe.append([nx, ny])

    # 만약 토마토들 중에 안 익은게 하나라도 있다면 -1 리턴하고 다 익었다면 걸린 날짜 반환
    for b in box:
        if 0 in b:
            return -1
    return days


m, n = map(int, stdin.readline().split())
box, ripe = [], deque()
for i in range(n):
    row = list(map(int, stdin.readline().split()))
    for j in range(m):
        # 익은 토마토가 있다면 익은 토마토 목록에 추가
        if row[j] == 1:
            ripe.append([i, j])
    box.append(row)

print(bfs(m, n, box))
