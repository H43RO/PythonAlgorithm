from sys import stdin

n, k = map(int, stdin.readline().split())
kinder = list(map(int, stdin.readline().split()))
result = []

# 인접한 유치원생들끼리의 키 차이를 모두 저장
for i in range(1, n):
    result.append(kinder[i] - kinder[i - 1])

# 이 키 차이 값들을 정렬했을 때, N-K 까지의 총합 출력
# N 명의 유치원 생을 K 조로 나눴기 때문
result.sort()

print(result)
print(sum(result[:n - k]))
