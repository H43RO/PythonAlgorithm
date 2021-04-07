n = int(input())

count = 1
pattern = 6
result = 1

while n > count:
    result += 1
    count += pattern
    pattern += 6

print(result)
