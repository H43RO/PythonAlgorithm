from sys import stdin

n = int(stdin.readline())
data = sorted([int(stdin.readline()) for _ in range(n)])
print(sum([abs(i - data[i - 1]) for i in range(1, n + 1)]))  # 정렬된 요소와 그 인덱스 간 차이가 총 불만도
