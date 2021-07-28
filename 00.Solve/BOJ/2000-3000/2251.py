from collections import deque
from sys import stdin

MAX_LITER = 201
a, b, c = map(int, stdin.readline().split())

# A, B 번 용량 상태 각각에 대한 방문 여부 저장하는 2차원 리스트
visited = [[False] * MAX_LITER for _ in range(MAX_LITER)]
result = []  # C 번 물통 용량 모든 경우의 수 저장

queue = deque([(0, 0, c)])
while queue:
    x, y, z = queue.popleft()
    if visited[x][y]:  # 해당 A, B 용량 상태를 방문한 적 있으면 패스
        continue

    visited[x][y] = True  # 방문 처리

    if x == 0:  # 만약 A 물통이 비어있다면, C 물통에 담긴 물의 양 저장
        result.append(z)

    # A 에서 B 로 물 붓는 시나리오 전개
    if x + y > b:  # A 물통 + B 물통 > B 물통 최대 용량
        queue.append((x + y - b, b, z))  # B 물통 가득 채우고 남은 만큼 A 남김
    else:  # A 물통 + B 물통 <= B 물통 최대 용량
        queue.append((0, x + y, z))  # A 물통에 있는 물 B 물통에 다 때려넣음

    # A 에서 C 로 물 붓는 시나리오 전개
    if x + z > c:  # A 물통 + C 물통 > C 물통 최대 용량
        queue.append((x + z - c, y, c))  # C 물통 가득 채우고 남은 만큼 A 남김
    else:  # A 물통 + C 물통 <= C 물통 최대 용량
        queue.append((0, y, x + z))  # A 물통에 있는 물 C 물통에 다 때려넣음

    # B 에서 A 로 물 붓는 시나리오 전개
    if y + x > a:  # B 물통 + A 물통 > A 물통 최대 용량
        queue.append((a, y + x - a, z))  # A 물통 가득 채우고 남은 만큼 B 남김
    else:  # B 물통 + A 물통 <= A 물통 최대 용량
        queue.append((y + x, 0, z))  # B 물통에 있는 물 A 물통에 다 때려넣음

    # B 에서 C 로 물 붓는 시나리오 전개
    if y + z > c:  # B 물통 + C 물통 > C 물통 최대 용량
        queue.append((x, y + z - c, c))  # C 물통 가득 채우고 남은 만큼 B 남김
    else:  # B 물통 + C 물통 <= C 물통 최대 용량
        queue.append((x, 0, y + z))  # B 물통에 있는 물 C 물통에 다 때려넣음

    # C 에서 A 로 물 붓는 시나리오 전개
    if z + x > a:  # C 물통 + A 물통 > A 물통 최대 용량
        queue.append((a, y, z + x - a))  # A 물통 가득 채우고 남은 만큼 C 남김
    else:  # C 물통 + A 물통 <= A 물통 최대 용량
        queue.append((z + x, y, 0))  # C 물통에 있는 물 A 물통에 다 때려넣음

    # C 에서 B 로 물 붓는 시나리오 전개
    if z + y > b:  # C 물통 + B 물통 > B 물통 최대 용량
        queue.append((x, b, z + y - b))  # C 물통 가득 채우고 남은 만큼 B 남김
    else:  # C 물통 + B 물통 <= B 물통 최대 용량
        queue.append((x, z + y, 0))  # C 물통에 있는 물 B 물통에 다 때려넣음

[print(x, end=' ') for x in sorted(result)]
