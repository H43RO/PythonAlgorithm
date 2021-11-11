from sys import stdin


def fill(length):
    global result
    if length % 4 == 0 or length % 2 == 0:  # 폴리오미노를 채울 수 있는지
        temp = ['AAAA'] * (length // 4)  # 4칸 짜리 우선으로 채우기
        temp += ['BB'] * (length % 4 // 2)  # 그 다음 2칸 짜리
        result += temp
        return True
    return False


board = list(stdin.readline().strip())
result = []

length = 0  # 폴리오미노 들어갈 자리의 길이
for i, v in enumerate(board):
    if v == '.':  # '.' 만날 경우
        if fill(length):  # 폴리오미노 채워보기
            length = 0
        else:  # 만약 채우기 불가능하다면 -1 출력후 종료
            print(-1)
            exit(0)
        result.append('.')  # 출력 결과에 '.' 추가
        continue
    length += 1  # '.' 이 아니였다면 길이 1 증가

if fill(length):  # 처리되지 않은 'X' 가 있다면
    length = 0
else:
    print(-1)
    exit(0)

print(''.join(result))
