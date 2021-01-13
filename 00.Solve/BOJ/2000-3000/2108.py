# 반올림 실수로 틀렸다가, round() 를 사용하여 정답 판정
# (반올림해야되는데 실수로 버림으로 구현함)

from collections import Counter
import sys

n = int(input())

data = []

for i in range(n):
    data.append(int(sys.stdin.readline()))

# 우선 입력받은 숫자들을 오름차순으로 정렬
data.sort()

# 각종 통계를 만들 수 있는 Counter 객체 생성
cnt = Counter(data)

# 각 원소의 등장 횟수를 담고 있는 튜플의 리스트를 얻는 함수
# 등장 횟수가 많은 원소 순으로 정렬되어 생성됨
order = cnt.most_common()

# 이제 같은 최빈값을 가진 원소들에 대한 처리 필요
# 문제에서 최빈값이 여러개일 때 두 번째로 작은 최빈값을 출력하라고 했기 때문

# 임의 초기값 설정 (우선 가장 맨 앞의 원소 등장 횟수로 지정)
maximum = order[0][1]

modes = []

# 등장 횟수들을 순환하면서, 또 다른 최빈값을 찾음
for num in order:
    if num[1] == maximum:
        modes.append((num[0]))

# 추가된 최빈값들을 오름차순으로 정렬
modes.sort()

# 산술 평균 출력 (round() 를 통해 소수점 이하 첫째 자리에서 반올림)
print(round(sum(data) / n))

# 중앙값 출력
print(data[n // 2])

# 만약 최빈값이 2개 이상이면 두 번째로 작은 값 출력
if len(modes) >= 2:
    print(modes[1])
# 만약 최빈값이 1개라면 그 값 그대로 출력
else:
    print(modes[0])

# 최댓값에서 최솟값을 뺀 범위 출력 (음 수일 수 있으므로 절대값 처리)
print(abs(max(data) - min(data)))
