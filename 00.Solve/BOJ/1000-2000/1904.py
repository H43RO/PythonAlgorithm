d = [0] * 1000001

n = int(input())

d[1] = 1
d[2] = 2

# 규칙이 거의 피보나치 수열임
for i in range(3, n + 1):
    d[i] = (d[i - 2] + d[i - 1]) % 15746

print(d[n])
