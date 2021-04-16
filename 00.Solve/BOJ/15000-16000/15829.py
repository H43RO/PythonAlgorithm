import string

alpha = string.ascii_lowercase

n = int(input())
m = 1234567891
data = list(input().strip())

result = 0

for i, v in enumerate(data):
    result += (alpha.index(v) + 1) * (31 ** i)

print(result % m)