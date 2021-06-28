import sys

sys.setrecursionlimit(10 ** 9)

n = int(sys.stdin.readline())
if n >= 1023:  # 1023번째 넘으면 1,000,000 범위 밖임
    print(-1)
elif n == 0:
    print(0)
else:
    cnt = 0
    num = 1
    while True:
        number = str(num)
        is_decreasing = True
        if len(number) == 1:  # 길이가 1이면 항상 감소하는 수
            pass
        else:
            for i in range(1, len(number)):
                if number[i] < number[i - 1]:
                    continue
                else:
                    is_decreasing = False
                    start = number[:i - 1]
                    mid = str(int(number[i - 1]) + 1)
                    end = '0' + number[i + 1:]
                    num = int(start + mid + end)
                    break
        if is_decreasing:
            cnt += 1
            if cnt == n:
                print(num)
                break
            num += 1
