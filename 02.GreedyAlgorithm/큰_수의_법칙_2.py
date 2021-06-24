from sys import stdin

n, m, k = map(int, stdin.readline().split())
data = sorted(list(map(int, stdin.readline().split())), reverse=True)
first = data[0]
second = data[1]

result = 0

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result += count * first  # 가장 큰 수 구하기
result += (m - count) * second  # 두 번째로 큰 수 더하기

print(result)
