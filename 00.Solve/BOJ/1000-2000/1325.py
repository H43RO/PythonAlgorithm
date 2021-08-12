from sys import stdin
from collections import deque


def bfs(start):
    visited = [False] * (n + 1)  # 매 탐색마다 방문정보 초기화
    visited[start] = True
    queue = deque([start])

    count = 1
    while queue:
        com = queue.popleft()
        for x in graph[com]:  # 연결 노드 정보가 있으면 BFS 순회
            if not visited[x]:  # 방문한 적 없는 노드로 이동
                visited[x] = True
                queue.append(x)
                count += 1

    return count  # 해킹한 컴퓨터의 수


n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[b].append(a)  # B 를 해킹하면 A 도 해킹할 수 있음 (연결된 노드)

hacking = []  # 여러 컴퓨터에서 최고 결과를 가질 수 있음
max_hacking = 0  # 최고 결과를 저장

for i in range(1, n + 1):      # 출발 컴퓨터 바꿔가며 BFS 탐색
    result = bfs(i)            # 해킹한 컴퓨터 수를 놓고 봤을 때
    if max_hacking < result:   # 역대 최고 결과라면
        max_hacking = result   # 최고 결과 갱신하고
        hacking = [i]          # hacking 도 해당 컴퓨터 번호로 초기화 해줌
        continue
    if max_hacking == result:  # 만약 최고 결과와 같은 결과를 받았다면
        hacking.append(i)      # hacking 리스트에 추가

print(*hacking)
