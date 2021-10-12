from sys import stdin
from collections import defaultdict

n = int(stdin.readline())
T = int(stdin.readline())

candidate = defaultdict(lambda: 0)  # 기본값을 0으로 가지는 dict()

for i, v in enumerate(list(map(int, stdin.readline().split()))):
    if len(candidate) == n and v not in candidate:  # 사진틀 꽉 차있고 추천받은 학생이 게시되어 있지 않다면 기존 사진틀 제거
        replace_index = list(candidate.values()).index(min(candidate.values()))  # 추천수가 가장 적은 후보 인덱스 저장
        del candidate[list(candidate.keys())[replace_index]]  # 해당 사진틀을 dict() 에서 제거

    candidate[v] += 1  # 추천수 1 증가

for x in sorted(candidate.keys()):  # 정렬된 최종 후보의 학생 번호 출력
    print(x, end=' ')
