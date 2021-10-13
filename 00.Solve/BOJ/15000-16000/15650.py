from sys import stdin, stdout

n, m = map(int, stdin.readline().split())

data = [0] * (m + 1)


def is_promising(data, i):
    """
    현재까지 수열이 비내림차순인지 검사하는 Pruning 함수
    :return: 조건에 만족하면 True, 아니라면 False
    """
    for j in range(1, i + 1):
        if data[j] == data[i] and i != j or data[j - 1] > data[j]:
            return False
    return True


def solve(data, count):
    """
    가능한 모든 수열을 만드는 함수
    """
    if count > m:  # 만약 M 길이의 수열이 완성되면
        for i in range(1, m + 1):
            print(data[i], end=' ')  # 출력
        print()
    else:
        for i in range(1, n + 1):
            data[count] = i  # 1 ~ N 까지의 숫자 차례대로 입력
            if is_promising(data, count):  # 만약 유망한 경우의 수가 맞다면
                solve(data, count + 1)  # 이어나감


solve(data, 1)
