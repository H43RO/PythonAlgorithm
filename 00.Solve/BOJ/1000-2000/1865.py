from sys import stdin

INF = int(1e9)


def bf(start, distance):
    distance[start] = 0
    for i in range(n):
        for x in edge:
            now, next, cost = x[0], x[1], x[2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[next] > distance[now] + cost:
                distance[next] = distance[now] + cost
                # n 번째 라운드에서도 값이 갱신되면 사이클 존재
                if i == n - 1:
                    return True
    return False


T = int(stdin.readline())
for _ in range(T):
    n, m, w = map(int, stdin.readline().split())
    edge = []
    distance = [INF] * (n + 1)
    for i in range(m):
        s, e, t = map(int, stdin.readline().split())
        edge.append((s, e, t))
        edge.append((e, s, t))
    for i in range(w):
        s, e, t = map(int, stdin.readline().split())
        edge.append((s, e, -t))

    print("YES" if bf(1, distance) else "NO")
