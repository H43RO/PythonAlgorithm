from sys import stdin

n, m, k = map(int, stdin.readline().split())
data = sorted(list(map(int, stdin.readline().split())), reverse=True)
first = data[0]
second = data[1]

result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
