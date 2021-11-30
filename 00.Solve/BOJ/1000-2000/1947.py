def solve(n):
    if n == 1:
        return False

    if n == 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


n = int(input())
graph = list(map(int, input().split()))

result = 0

for i in graph:
    if solve(i):
        result += 1

print(result)
