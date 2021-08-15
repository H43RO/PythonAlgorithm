from sys import stdin

N, L = map(int, stdin.readline().split())
water = sorted(list(map(int, stdin.readline().split())))

start = water[0]
end = start + L - 1

result = 1
for x in water:
    if start <= x <= end:
        continue
    start = x
    end = start + L - 1
    result += 1

print(result)
