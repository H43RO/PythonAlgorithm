from sys import stdin

n = int(stdin.readline())
# 입력이 1,000,000 이기 때문에 좀 더 큰 값까지 찾아봐야 함
m = 1_100_000

# 특정 숫자(인덱스)가 소수면 True, 아니면 False 로 저장
prime = [True] * m

# 에라토스테네스의 체를 활용하여 소수 리스트 만듦
for i in range(2, int(m ** 0.5) + 1):
    if prime[i]:
        for j in range(i + i, m, i):
            prime[j] = False

result = 0

# N 부터 끝까지 탐색
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

print(result)
