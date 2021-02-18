from sys import stdin, stdout


def check(num):
    global disabled
    for x in str(num):
        if int(x) in disabled:
            return False
    return True


n = int(stdin.readline().strip())
m = int(stdin.readline().strip())

if m >= 1:
    disabled = list(map(int, stdin.readline().split()))
else:
    disabled = []

result = abs(n - 100)

for i in range(1000001):
    if check(i):
        result = min(result, len(str(i)) + abs(i - n))

print(result)
