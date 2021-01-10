from sys import stdin, stdout
from collections import deque

n, k = map(int, stdin.readline().split())
visited = [0] * 100001


def bfs(v):
    count = 0  # 점을 몇 번 이동했는지에 대한 정보 기록
    queue = deque([[v, count]])  # Queue 에 최초 위치(N)와 이동 거리(0회) 삽입

    while queue:
        q = queue.popleft()
        current = q[0]  # 현재 위치 정보를 꺼내옴
        count = q[1]  # 현재 까지 이동한 횟수 정보를 꺼내옴

        # 현재 위치를 방문한 적이 없다면 방문으로 기록하고 이후 태스크 시작
        if not visited[current]:
            visited[current] = True

            # 현재 위치가 목적지라면 지금껏 이동한 횟수 정보 반환
            if current == k:
                return count

            # 현재 위치가 목적지가 아니라면 우선 이동 횟수 증가
            count += 1

            # 이동 가능한 범위 내에서 이동 (Queue 에 위치와 이동 거리(횟수) 삽입)
            if 0 <= current - 1 <= 100000:
                queue.append([current - 1, count])
            if 0 <= current + 1 <= 100000:
                queue.append([current + 1, count])
            if 0 <= current * 2 <= 100000:
                queue.append([current * 2, count])

    return count


print(bfs(n))
