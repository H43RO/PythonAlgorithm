from sys import stdin
import heapq

INF = int(1e9)


def dijkstra(start):
    distance = [INF] * (n + 1)  # 최단 거리 테이블을 모두 무한 값으로 초기화
    q = []
    heapq.heappush(q, (0, start))  # (현재 최단 거리, 해당 노드) 튜플로 저장
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)  # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 (힙의 특성 사용)
        if distance[now] < dist:  # 이미 최단 경로가 저장되어 있다면 무시
            continue
        for i in graph[now]:  # 현재 노드와 연결된 다른 인접한 노드들을 확인
            cost = dist + i[1]
            if cost < distance[i[0]]:  # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    result = 0
    for i in range(1, n + 1):
        if distance[i] <= m:  # 수색 반경 M 안의 아이템 모두 저장
            result += item[i]

    return result  # 아이템 수 리턴


n, m, r = map(int, stdin.readline().split())
item = [0] + list(map(int, stdin.readline().split()))  # 노드 인덱싱 편의상 맨 앞에 임의로 0 추가
graph = [[] for _ in range(n + 1)]  # 인접노드 정보를 담을 그래프

for _ in range(r):  # 양방향 순회 쌉 가능하게 간선 정보 모두 담아줌
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

max_item = 0
for i in range(1, n + 1):
    temp = dijkstra(i)  # 모든 노드를 기점으로 다익스트라를 수행해보면서
    max_item = max(max_item, temp)  # 최대로 습득할 수 있는 아이템 개수만을 저장
print(max_item)
