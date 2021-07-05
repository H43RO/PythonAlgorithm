from sys import stdin

n, k = map(int, stdin.readline().split())
dp = [0] * (k + 1)
dp[0] = 1

coin = []
for _ in range(n):
    coin.append(int(stdin.readline()))

'''
    [핵심 아이디어]
    사용할 수 있는 동전 세트를 하나씩 늘려가면서 루프를 돌아줌
    루프마다 '사용 가능한 동전을 모두 사용하여' 특정 수를 만들 수 있는 경우의 수를 늘려가면
    최종적으로 K 를 만들 수 있는 경우의 수를 뽑아낼 수 있음 (경우의 수 누적 형식)
'''
for x in coin:
    for i in range(x, k + 1):
        dp[i] += dp[i - x]

print(dp[k])
