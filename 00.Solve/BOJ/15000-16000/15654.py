from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
num = list(map(int, stdin.readline().split()))
num.sort()

data = [0] * (m + 1)


def is_promising(data, i):
    for j in range(1, i + 1):
        if data[j] == data[i] and i != j:  # 모든 수가 달라야 함
            return False
    return True


def solve(data, count):
    if count > m:  # 길이가 M 이 되었을 경우 출력
        for i in range(1, m + 1):
            print(data[i], end=' ')
        print()
    else:
        for x in num:
            data[count] = x
            if is_promising(data, count):  # 유망한 경우의 수라면
                solve(data, count + 1)  # 경우의 수 계속 뻗어나감


solve(data, 1)
