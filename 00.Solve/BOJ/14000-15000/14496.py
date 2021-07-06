from sys import stdin, stdout
import heapq

INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # (현재 최단 거리, 해당 노드) 튜플로 저장
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)  # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        if distance[now] < dist:  # 이미 최단 경로가 저장되어 있다면 무시
            continue
        for x in graph[now]:  # 현재 노드와 연결된 다른 인접한 노드들을 확인
            cost = dist + 1  # 치환 횟수 1 증가
            if cost < distance[x]:  # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[x] = cost  # 최단 거리 갱신 (최소 치환 횟수 갱신)
                heapq.heappush(q, (cost, x))


start, end = map(int, stdin.readline().split())
n, m = map(int, stdin.readline().split())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)  # 최소 치환횟수 (최단 거리) 테이블을 모두 무한 값으로 초기화

for _ in range(m):  # 양방향 순회 쌉 가능하게 간선 정보 모두 담아줌
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)  # '치환을 몇 번 했냐' 를 노드 이동 비용으로 둘 때
    graph[b].append(a)  # 횟수는 항상 1씩 늘어나므로 이동 비용 따로 안 넣음

dijkstra(start)

print(distance[end] if distance[end] != INF else -1)