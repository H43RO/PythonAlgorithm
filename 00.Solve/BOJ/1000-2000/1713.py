from sys import stdin
from collections import defaultdict

n = int(stdin.readline())
T = int(stdin.readline())

candidate = defaultdict(lambda: 0)

for i, v in enumerate(list(map(int, stdin.readline().split()))):
    if len(candidate) == n and v not in candidate:  # 사진틀 꽉 차있는 경우 교체 작업
        replace_index = list(candidate.values()).index(min(candidate.values()))  # 최소 추천수 사진틀의 인덱스 (인덱스 가장 낮은 녀석)
        del candidate[list(candidate.keys())[replace_index]]  # 해당 사진틀을 dict() 에서 제거

    candidate[v] += 1  # 추천수 1 증가

for x in sorted(candidate.keys()):
    print(x, end=' ')
