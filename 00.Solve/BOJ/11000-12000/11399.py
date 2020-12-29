n = int(input())

result = 0

num = list(map(int, input().split()))

time = sorted(num)

for i in range(len(time)):
    result += (sum(time[:i + 1]))

print(result)
