from sys import stdin, stdout

n = int(stdin.readline())
k = int(stdin.readline())

# 같은 좌표에 있는 센서 중복 제거
sensors = list(map(int, stdin.readline().split()))
sensors.sort()

data = []

for i in range(1, len(sensors)):
    data.append(sensors[i] - sensors[i - 1])

data.sort()

for i in range(k - 1):
    if len(data) == 0:
        data.append(0)
        break
    else:
        data.pop()

print(sum(data))
