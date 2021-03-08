from sys import stdin

n, m = map(int, stdin.readline().split())

data = [0] * (m + 1)


# 유망성 검사
def is_promising(data, i):
    # 현재 조사 중인 인덱스까지 탐색했을 때
    for j in range(1, i + 1):
        # 중복된 값이 발견되면 가지 치기 (Pruning)
        if data[j] == data[i] and i != j:
            return False
    return True


def solve(data, count):
    # 조건을 만족하는 수열이 완성되면 출력
    if count > m:
        for i in range(1, m + 1):
            print(data[i], end=' ')
        print()
    else:
        # 인덱스 순서 차례대로 1 ~ n 까지 늘려보면서 유망성 검사
        # - 유망성 검사 통과 시, 재귀 호출
        for i in range(1, n + 1):
            data[count] = i
            if is_promising(data, count):
                solve(data, count + 1)


solve(data, 1)
