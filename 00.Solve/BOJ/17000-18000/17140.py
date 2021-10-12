from sys import stdin


def sort_graph(graph, command):
    result = []

    if command == "C":  # 편의를 위해 회전
        graph = list(map(list, zip(*graph)))

    for x in graph:
        temp = []
        count = []
        for a in set(x):
            if a == 0:
                continue
            count.append((a, x.count(a)))
        for num, cnt in sorted(count, key=lambda x: (x[1], x[0])):
            temp.extend([num, cnt])
        result.append(temp)

    for x in result:
        while len(x) < len(max(result, key=lambda x: len(x))):
            x.append(0)
        x = x[:100]

    if command == "C":
        result = list(map(list, zip(*result)))  # 90도 회전

    return result


r, c, k = map(int, stdin.readline().split())
data = [list(map(int, stdin.readline().split())) for _ in range(3)]

for i in range(101):
    if 0 <= r - 1 < len(data) and 0 <= c - 1 < len(data[0]) and data[r - 1][c - 1] == k:
        print(i)
        exit(0)

    command = "R" if len(data) >= len(data[0]) else "C"
    data = sort_graph(data, command)

print(-1)
