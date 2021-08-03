from sys import stdin

n = int(stdin.readline())
distance = list(map(int, stdin.readline().split()))
price = list(map(int, stdin.readline().split()))

min_price = price[0]  # 최소 비용 (최소 비용 만날 때마다 갱신)
result = distance[0] * min_price  # 처음엔 무조건 기름 넣어야 함

for i in range(1, n - 1):
    if min_price > price[i]:  # 최소 비용 만나면 갱신
        min_price = price[i]
    result += distance[i] * min_price  # 도시 이동할 때마다 최소비용으로 주유

print(result)
