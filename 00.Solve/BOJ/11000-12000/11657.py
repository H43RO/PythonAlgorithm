from sys import stdin

INF = int(1e9)


def bf(start):
    distance[start] = 0
    for i in range(n):
        # 매 반복마다 "모든 간선"을 확인하며
        for j in range(m):
            # now 에서 next 로 가는 비용이 cost
            now = edges[j][0]
            next = edges[j][1]
            cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[now] != INF and distance[next] > distance[now] + cost:
                distance[next] = distance[now] + cost

                # n 번째 라운드에서도 값이 갱신되면 즉시 종료
                if i == n - 1:
                    return True
    return False


n, m = map(int, stdin.readline().split())  # 노드 개수, 간선 개수 입력
edges = []  # 모든 간선에 대한 정보를 담는 리스트
distance = [INF] * (n + 1)  # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m):  # 모든 간선 정보 입력받음
    a, b, c = map(int, stdin.readline().split())
    edges.append((a, b, c))  # a 에서 b 로 가는 비용이 c

# 벨만 포드 알고리즘 수행
negative_cycle = bf(1)  # 음수 사이클이 있다면 True 담김

if negative_cycle:  # 음수 사이클이 있다 -> 즉시 종료
    print("-1")
    exit()

# 1번 노드 제외 다른 모든 노드로 가기 위한 최단 거리 출력
for i in range(2, n + 1):
    # 도달할 수 없는 경우 -1
    # 도달할 수 있는 경우 그 최단 거리를 출력
    print(distance[i] if distance[i] != INF else -1)
