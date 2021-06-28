from sys import stdin

n = int(stdin.readline())
num = list(map(str, stdin.readline().split()))
num.sort(key=lambda x: x * 3, reverse=True)

print(str(int(''.join(num))))
