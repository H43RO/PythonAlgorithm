import heapq


def solution(n, edge):
    answer = 0

    INF = int(1e9)
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    for x in edge:
        a, b = x[0], x[1]
        # 양방향 그래프이기 때문에
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    start = 1
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for x in graph[now]:
            cost = dist + x[1]
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(q, (cost, x[0]))

    while INF in distance:
        distance.remove(INF)

    answer = distance.count(max(distance))

    return answer


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
