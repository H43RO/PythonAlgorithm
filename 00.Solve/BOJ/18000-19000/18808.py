from sys import stdin


# 스티커를 90도 회전 시키는 함수
def rotated(sticker):
    n = len(sticker)
    m = len(sticker[0])
    rotated_sticker = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            rotated_sticker[j][n - i - 1] = sticker[i][j]
    return rotated_sticker


# 스티커를 붙일 수 있는지에 대한 결과 반환 함수
def available(x, y, sticker):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == 0:
                continue
            if graph[x + i][y + j] == 1:
                return False
    return True


# available() 검사가 끝난 후 스티커를 붙이는 함수
def attach_sticker(x, y, sticker):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == 1:
                # 시작점으로부터 (행 + i, 열 + j) 위치에 스티커 부착
                graph[x + i][y + j] = 1


n, m, k = map(int, stdin.readline().split())
graph = [[0] * m for _ in range(n)]

stickers = []

# 스티커 정보 저장
for _ in range(k):
    r, c = map(int, stdin.readline().split())
    temp = []
    for i in range(r):
        temp.append(list(map(int, stdin.readline().split())))
    stickers.append(temp)

# 스티커 각각에 대하여 순서대로 탐색
for x in stickers:
    sticker = x
    r = len(sticker)
    c = len(sticker[0])
    # 0, 90, 180, 270도 각각에 대하여 경우의 수 고려
    for _ in range(4):
        # 만약 노트북 크기에 안 맞는 스티커면 회전 시도
        if n < r or m < c:
            r, c, sticker = c, r, rotated(sticker)
            continue
        # 스티커를 붙이는 데에 성공했는지에 대한 플래그 변수
        flag = False
        # 스티커 사이즈 고려하여 탐색
        for i in range(n - r + 1):
            for j in range(m - c + 1):
                # 스티커를 붙일 수 있는 공간이 있는지 탐색
                if not available(i, j, sticker):
                    continue
                # 공간이 있다면 노트북에 스티커 붙이고 플래그 활성화
                attach_sticker(i, j, sticker)
                flag = True
                break
            if flag:
                break
        if flag:
            break

        # 만약 스티커를 붙이지 못하였다면 회전
        r, c, sticker = c, r, rotated(sticker)

# 스티커가 차지하는 영역 개수 출력
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            result += 1
print(result)
