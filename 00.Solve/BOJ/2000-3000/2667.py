n = int(input())

graph = []

result = 0

counts = []
count = 0

for i in range(n):
    graph.append(list(map(int, input())))


def dfs_function(x, y):
    global count
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        dfs_function(x - 1, y)
        dfs_function(x + 1, y)
        dfs_function(x, y - 1)
        dfs_function(x, y + 1)
        return True
    return False


for i in range(n):
    for j in range(n):
        if dfs_function(i, j) == True:
            result += 1
            counts.append(count)
            count = 0


print(result)

counts.sort()
for x in counts:
    print(x)
