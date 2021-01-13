def solve(n, m):
    result = [True] * (m + 1)

    result[1] = False

    for i in range(2, m + 1):
        if result[i]:
            for j in range(i + i, m + 1, i):  # start, stop, step
                result[j] = False

    return result


n, m = map(int, input().split())

result = solve(n, m)

for x in range(n, len(result)):
    if result[x]:
        print(x)
