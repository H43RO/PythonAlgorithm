from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))

comb = list(combinations(card, 3))  # 조합
card_sum = []

for x in comb:
    if sum(x) <= m:
        card_sum.append(sum(x))

print(max(card_sum))
