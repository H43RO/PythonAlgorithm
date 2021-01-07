n = int(input())
result = [0] * n

for i in range(n):
    data = input()
    score = 0
    for v in data:
        # O 만날 때 마다 점수 증가
        if v == 'O':
            score += 1
            result[i] += score

        # X 만나는 순간 점수 초기화
        if v == 'X':
            score = 0

for x in result:
    print(x)
