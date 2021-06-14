from sys import stdin

n = int(stdin.readline())
result = 0

for _ in range(n):
    dice = list(map(int, stdin.readline().split()))
    data = set(dice)

    if len(data) == 3:
        result = max(result, max(dice) * 100)
    elif len(data) == 2:
        if dice.count(dice[0]) == 2:
            result = max(result, 1000 + dice[0] * 100)
        else:
            result = max(result, 1000 + dice[1] * 100)
    elif len(data) == 1:
        result = max(result, 10000 + dice[0] * 1000)

print(result)
