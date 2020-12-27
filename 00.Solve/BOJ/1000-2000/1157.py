input = list(input().upper())

alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
result = [0] * len(alpha)

for x in input:
    result[alpha.index(x)] += 1

output = alpha[result.index(max(result))]

if result.count(max(result)) > 1:
    output = '?'

print(output)