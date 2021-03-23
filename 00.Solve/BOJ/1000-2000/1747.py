from sys import stdin

n = int(stdin.readline())
m = 1_000_001
prime = [True] * m

# 에라토스테네스의 체를 활용하여 소수 리스트 만듦
for i in range(2, int(m ** 0.5) + 1):
    if prime[i]:
        for j in range(i + i, m, i):
            prime[j] = False

result = 0

# N 부터 1,000,001 까지 탐색
while n < m:
    if n == 1:
        result = 2
        break
    num = str(n)
    if num == num[::-1] and prime[n]:
        result = n
        break
    n += 1

if result == 0:
    print(1003001)
else:
    print(result)
