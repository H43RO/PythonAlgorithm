from sys import stdin
import heapq

# 옵티멀 아이디어 :  항상 가장 큰 슬라임 두 개를 꺼내야 함

n = int(stdin.readline())

slime = []
for x in list(map(int, stdin.readline().split())):
    slime.append((-x, x))  # 슬라임 데이터를 최대 힙에 넣음

score = 0
while len(slime) > 1:
    _, x = heapq.heappop(slime)
    _, y = heapq.heappop(slime)
    heapq.heappush(slime, (-(x + y), x + y))  # x + y 를 힙에 추가
    score += x * y  # x * y 만큼 점수 추가

print(score)
