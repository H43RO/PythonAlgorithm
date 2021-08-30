import copy


# 왼쪽으로 90도 회전
def rotate_left(key):
    result = []
    for i in range(len(key) - 1, -1, -1):
        temp = []
        for j in range(len(key)):
            temp.append(key[j][i])
        result.append(temp)
    return result


# 오른쪽으로 90도 회전
def rotate_right(key):
    result = []
    for i in range(len(key)):
        temp = []
        for j in range(len(key) - 1, -1, -1):
            temp.append(key[j][i])
        result.append(temp)
    return result


# 끼워맞춰지는 부분이 있는지 탐색
def find(key, lock):
    n = len(key)   # 열쇠 한 변 길이
    m = len(lock)  # 자물쇠 한 변 길이
    graph = [[0] * (m * 3) for _ in range(m * 3)]  # 그래프 확장

    # 확장한 그래프 가운데 즈음에 키 그리기
    for i in range(m, m + n):
        for j in range(m, m + n):
            graph[i][j] = key[i - m][j - m]

    # 그래프를 탐색하며 열쇠와 자물쇠 맞물리는 부분 탐색
    for i in range(m * 2):
        for j in range(m * 2):
            available = True
            for k in range(i, i + m):
                for u in range(j, j + m):
                    # 영역 내 모든 원소가 달라야 맞물리는 것
                    if graph[k][u] == lock[k - i][u - j]:
                        available = False
            if available:
                return True
    return False


def solution(key, lock):
    # 오른쪽으로 4번 회전해보면서 탐색 (360도 회전이므로 원본 포함)
    original = copy.deepcopy(key)
    for i in range(4):
        temp = rotate_right(original)
        # 탐색
        if find(original, lock):
            return True
        original = temp

    # 왼쪽으로 3번 회전해보면서 탐색
    original = copy.deepcopy(key)
    for i in range(3):
        temp = rotate_left(original)
        # 탐색
        if find(original, lock):
            return True
        original = temp

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

# 50분 소요
