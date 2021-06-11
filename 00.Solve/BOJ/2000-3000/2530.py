A, B, C = map(int, input().split())
D = int(input())

t = A * 60 * 60 + B * 60 + C + D
h = t // 60 // 60 % 24
m = t // 60 % 60
s = t % 60

print(h, m, s)
