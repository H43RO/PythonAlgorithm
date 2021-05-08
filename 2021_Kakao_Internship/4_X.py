import heapq

INF = int(1e9)


def solution(n, start, end, roads, traps):
    answer = 0

    # 각 노드에 연결되어 있는 노드에 대한 정보(튜플)를 담는 리스트를 만들기
    graph = [[] for i in range(n + 1)]
    # 최단 거리 테이블을 모두 무한 값으로 초기화
    distance = [INF] * (n + 1)

    # 모든 간선 정보를 입력받기
    for x in roads:
        a, b, c = x[0], x[1], x[2]
        # a 번 노드에서 b 번 노드로 가는 비용이 c 라는 의미
        graph[a].append((b, c))

    print(graph)

    q = []
    # 시작 노드를 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입 (시작점 그 자리 그대니까)
    # (현재 최단 거리, 해당 노드) 튜플로 저장
    heapq.heappush(q, (0, start))
    distance[start] = 0


    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 (힙의 특성 사용)
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        # - 즉, 이미 최단 경로가 저장되어 있다면 무시
        if distance[now] < dist:
            continue

        # 트랩에 도착했다면 트랩과 연결된 모든 경로를 반대로!
        if now in traps:
            # 트랩에서 나가는 경로를 모두 들어오는 경로로
            for x in graph[now]:
                a, b, c = x[0], now, x[1]
                graph[a].append((b, c))
                graph[now].remove(x)
            # 트랩으로 진입하는 경로를 모두 나가는 경로로
            for i in range(len(graph)):
                for j in range(len(graph[i])):
                    if graph[i][j][0] == now:
                        a, b, c = i, now, graph[i][j][1]
                        graph[a].append((b, c))
                        graph[i].remove(graph[i][j])
            heapq.heappush(q, (dist, now))
            continue

        print(graph)
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))



    return distance[end]


print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
