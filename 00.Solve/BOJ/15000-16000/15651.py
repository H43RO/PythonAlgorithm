from sys import stdin

n, m = map(int, stdin.readline().split())
data = [0] * (m + 1)


def solve(data, count):
    if count > m:  # 수열이 m 만큼 채워졌을 때
        print(*data[1:])
    else:
        for i in range(1, n + 1):  # 각 자리에서 모든 경우의 수 가지 뻗기
            data[count] = i
            solve(data, count + 1)


solve(data, 1)
