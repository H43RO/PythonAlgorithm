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
    # 만약 N 이 1 이라면 2가 답임
    if n == 1:
        result = 2
        break
    num = str(n)
    # 팰린드롬이자 소수라면 결과 저장
    if num == num[::-1] and prime[n]:
        result = n
        break
    n += 1

# 결과가 없다면 1000001 보다 크고 팰린드롬이자 소수인 1003001 이 결과임
if result == 0:
    print(1003001)
else:
    print(result)
