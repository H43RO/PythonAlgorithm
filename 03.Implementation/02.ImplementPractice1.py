# 완전 탐색으로 해결 가능 (Brute Force)

n = int(input())

result = 0

for hour in range(n+1):
    for minute in range(60):
        for second in range(60):
            if '3' in str(second) + str(minute) + str(hour):
                result += 1

print(result)
