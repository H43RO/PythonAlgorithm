from sys import stdin, stdout

case = int(stdin.readline().strip())
results = []

for _ in range(case):
    n = int(stdin.readline().strip())

    people = []
    for i in range(n):
        people.append(tuple(map(int, stdin.readline().split())))

    # 서류 점수로 정렬
    people.sort()

    # 가장 우수한 면접 점수 저장하는 변수
    interview_min = people[0][1]
    del people[0]

    # 서류 점수가 가장 우수한 첫 번째 사람은 무조건 뽑힘
    count = 1

    # 매번 가장 우수한 면접 점수와 비교하여 면접 점수가 더 우수하면 합격 (어차피 서류는 밀림)
    for x in people:
        if interview_min > x[1]:
            count += 1
            interview_min = x[1]
        else:
            continue
    results.append(count)

for x in results:
    print(x)
