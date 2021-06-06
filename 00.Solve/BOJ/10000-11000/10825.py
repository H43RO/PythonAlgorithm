from sys import stdin

n = int(stdin.readline())
data = []

for _ in range(n):
    data.append(list(stdin.readline().split()))

# sort 함수의 key 파라미터를 활용하여 정렬 우선순위 지정
# 예를들어 2번째 키는 1번째 키 값이 같은 원소 (국어 점수가 같은 원소) 에 대한 정렬 기준
# 그리고 3번째 키는 2번째 키 값이 같은 원소 (국어, 영어 점수가 같은 원소) 에 대한 정렬 기준
data.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for x in data:
    print(x[0])
