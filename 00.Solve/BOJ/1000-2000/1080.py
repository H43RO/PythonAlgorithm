from sys import stdin, stdout


def invert(graph, i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            graph[x][y] = abs(graph[x][y] - 1)


n, m = map(int, stdin.readline().split())
count = 0

A = [list(map(int, stdin.readline().strip())) for _ in range(n)]
B = [list(map(int, stdin.readline().strip())) for _ in range(n)]

for i in range(n - 2):
    for j in range(m - 2):
        if A[i][j] != B[i][j]:
            invert(A, i, j)
            count += 1

no_answer = False
for i in range(n):
    for j in range(m):
        if A[i][j] != B[i][j]:
            no_answer = True

if no_answer:
    print(-1)
else:
    print(count)