n = int(input())

result = 0

num = list(map(int, input().split()))

# 짧게 걸리는 순으로 정렬
time = sorted(num)

for i in range(len(time)):
    result += (sum(time[:i + 1]))

print(result)
