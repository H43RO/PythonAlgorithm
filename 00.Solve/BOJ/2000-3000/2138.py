import copy
from sys import stdin, exit


# 규칙에 맞게 전구의 상태를 바꿔주는 스위치 함수
def switch(bulb, n, i):
    global count
    count += 1
    bulb[i] *= -1
    if i == 0:
        bulb[i + 1] *= -1
    elif i == n - 1:
        bulb[i - 1] *= -1
    else:
        bulb[i - 1] *= -1
        bulb[i + 1] *= -1

    if bulb == target:
        print(count)
        exit()


n = int(stdin.readline())
bulb = list(map(int, stdin.readline().strip()))
target = list(map(int, stdin.readline().strip()))

# 연산 편의 상 1 과 -1 두 상태를 갖도록 함 (상태 전환으로써 *= -1 연산이 가능)
for i in range(n):
    if bulb[i] == 0:
        bulb[i] = -1
    if target[i] == 0:
        target[i] = -1

# 처음부터 똑같은 두 개가 들어온 경우 바로 종료
if bulb == target:
    print(0)
    exit()

# 최악의 경우 두 번의 탐색이 이루어지기 때문에 미리 초기 상태 복사
bulb2 = copy.deepcopy(bulb)

count = 0
# 첫 번째 전구를 누르는 경우
for i in range(n):
    if i == 0:
        switch(bulb, n, i)
    # 이전 전구 상태가 타겟과 다를 때 현재 스위치 누르기
    elif bulb[i - 1] != target[i - 1]:
        switch(bulb, n, i)

count = 0
# 첫 번째 전구를 누르지 않는 경우
for i in range(1, n):
    # 이전 전구 상태가 타겟과 다를 때 현재 스위치 누르기
    if bulb2[i - 1] != target[i - 1]:
        switch(bulb2, n, i)

print(-1)
