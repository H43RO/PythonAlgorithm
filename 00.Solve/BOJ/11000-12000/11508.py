from sys import stdin

# 옵티멀 아이디어
# - 유제품 가격을 내림차순으로 정렬하면 가격이 높은 유제품을 공짜로 사는 경우가 많아짐 (최소비용 유도 가능)

n = int(stdin.readline())
data = sorted([int(stdin.readline()) for _ in range(n)], reverse=True)

result = 0
for i in range(n):
    if i % 3 != 2:  # 가장 싼 것은 무료로 지불, 나머지 두 개 가격 지불
        result += data[i]

print(result)
