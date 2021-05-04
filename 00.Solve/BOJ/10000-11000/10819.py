from itertools import permutations

n = int(input())
num = list(map(int, input().split()))

# 입력 범위가 크지않아, 가능한 모든 경우의 순열 리스트 생성
data = list(permutations(num, n))
result = []

for x in data:
    temp = 0
    # 주어진 식에 맞추어 동작 후 결과 저장
    for i in range(n - 1):
        temp += abs(x[i] - x[i + 1])
    result.append(temp)

# 얻을 수 있는 가장 큰 값 출력
print(max(result))