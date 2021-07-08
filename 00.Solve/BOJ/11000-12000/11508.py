from sys import stdin

# 옵티멀 아이디어
# - 유제품 가격을 내림차순으로 정렬하면 가격이 높은 유제품을 공짜로 사는 경우가 많아짐

n = int(stdin.readline())
data = sorted([int(stdin.readline()) for _ in range(n)], reverse=True)

result = 0
for i in range(n):
    if i % 3 != 2:
        result += data[i]

print(result)
