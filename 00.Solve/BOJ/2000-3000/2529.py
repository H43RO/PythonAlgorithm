from itertools import permutations

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

k = int(input())
sign = list(input().split())

data = list(permutations(num, k + 1))

result = []

for x in data:
    is_able = True
    for i in range(k):
        # 부등호 순서대로 조건에 부합하는지 검사
        if sign[i] == '>' and x[i] > x[i + 1]:
            continue
        elif sign[i] == '<' and x[i] < x[i + 1]:
            continue
        # 조건을 만족 못하는 경우
        is_able = False
        break

    if is_able:
        result.append(''.join(map(str, x)))

print(max(result))
print(min(result))
