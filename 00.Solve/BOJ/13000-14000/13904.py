from sys import stdin, stdout

homework = []
n = int(stdin.readline())
for i in range(n):
    homework.append(tuple(map(int, stdin.readline().split())))

# 마감일 많이 남은 순으로 정렬하고, 매 회차 최댓값만 고르면 됨
homework.sort(reverse=True, key=lambda x: x[0])

day = homework[0][0]
result = 0

# 날짜를 줄여가며 탐색
while day > 0:
    data = []

    # 과제 목록에서 현재 날짜 이상으로 마감일이 남은 과제 저장
    for x in homework:
        if x[0] >= day:
            data.append(x)

    # 만약 당일 수행할 수 있는 과제가 없다면 다음 날로 이동
    if not data:
        day -= 1
        continue

    # 고른 과제들 중 점수가 가장 큰 과제를 결과에 저장하고, 목록에서 제외
    temp = max(data, key=lambda x: x[1])
    result += temp[1]
    del homework[homework.index(temp)]
    day -= 1

print(result)
