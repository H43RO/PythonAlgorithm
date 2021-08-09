from sys import stdin
import heapq

n = int(stdin.readline())

slime = []
for x in list(map(int, stdin.readline().split())):
    slime.append((-x, x))  # 슬라임 데이터를 최대 힙에 넣음

score = 0
while len(slime) > 1:
    _, x = heapq.heappop(slime)
    _, y = heapq.heappop(slime)
    heapq.heappush(slime, (-(x + y), x + y))
    score += x * y

print(score)
