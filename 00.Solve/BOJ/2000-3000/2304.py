from sys import stdin

n = int(stdin.readline())
# 왼쪽 면 위치 L, 높이 H

pillar = dict()

for _ in range(n):
    L, H = map(int, stdin.readline().split())
    pillar[L] = H

max_pillar = max(pillar, key=pillar.get)  # 가장 높은 높이의 기둥 번호
result = pillar[max_pillar]

temp = 0
for i in range(0, max_pillar):
    if i in pillar:
        temp = max(temp, pillar[i])
    result += temp

temp = 0
for i in range(max(pillar.keys()), max_pillar, -1):
    if i in pillar:
        temp = max(temp, pillar[i])
    result += temp

print(result)
