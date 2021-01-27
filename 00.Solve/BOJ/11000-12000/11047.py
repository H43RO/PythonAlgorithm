n, k = map(int, input().split())

coins = []

for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)  # 내림차순 정렬 (큰 단위부터 차례대로)

result = 0

for coin in coins:
    if coin <= k:
        result += (k // coin)
        k = k % coin

print(result)
