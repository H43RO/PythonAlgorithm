from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))

comb = list(combinations(card, 3))  # 카드 3개를 뽑는 조합 리스트
card_sum = []

for x in comb:
    # M 을 넘지 않는 모든 값 저장
    if sum(x) <= m:
        card_sum.append(sum(x))

# 저장한 값들 중 가장 큰 값 출력
print(max(card_sum))
