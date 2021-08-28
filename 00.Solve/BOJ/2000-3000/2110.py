from sys import stdin

n, c = map(int, stdin.readline().split())
house = [int(stdin.readline()) for _ in range(n)]

# 1. 첫 번째 집, 마지막 번째 집 좌표에 공유기 2개 설치 (최소 2개 이상 주어짐)
