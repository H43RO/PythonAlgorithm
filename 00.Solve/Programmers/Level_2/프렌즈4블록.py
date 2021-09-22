def explode(data, m, n):
    explosion = set()

    # 폭발할 수 있는 세트 탐색
    for i in range(1, n):
        for j in range(1, m):
            if data[i][j] == data[i - 1][j - 1] == data[i - 1][j] == data[i][j - 1] is not None:
                explosion |= {(i, j), (i - 1, j - 1), (i - 1, j), (i, j - 1)}

    for i, j in explosion:
        data[i][j] = 0

    for i, v in enumerate(data):
        empty = [None] * v.count(0)  # 폭발 개수만큼 None 생성
        data[i] = empty + [x for x in v if x != 0]  # 중력 처리

    return len(explosion)


def solution(m, n, board):
    count = 0
    data = list(map(list, zip(*board)))  # 90도 회전
    while True:
        pop = explode(data, m, n)
        if pop == 0:
            return count
        count += pop


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
