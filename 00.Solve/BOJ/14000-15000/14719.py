from sys import stdin

h, w = map(int, stdin.readline().split())
graph = [[0] * w for _ in range(h)]
height = list(map(int, stdin.readline().split()))
for i in range(w):
    for j in range(h - height[i], h):
        graph[j][i] = 1

# 핵심 아이디어 : 기둥 사이의 거리로 고인 빗물 계산
result = 0
for x in graph:
    # 만약 기둥이 하나밖에 없다면 물 못 채움
    if x.count(1) <= 1:
        continue
    pillar = []
    # 기둥의 인덱스를 모두 저장
    for i in range(w):
        if x[i] == 1:
            pillar.append(i)
    for i in range(1, len(pillar)):
        result += pillar[i] - pillar[i - 1] - 1

print(result)
