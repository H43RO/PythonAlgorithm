dial = [[2, 'ABC'], [3, 'DEF'], [4, 'GHI'],
        [5, 'JKL'], [6, 'MNO'], [7, 'PQRS'],
        [8, 'TUV'], [9, 'WXYZ']]

# 번호 + 1 이 금속 핀까지 돌리는 데 걸리는 시간

input = input()
result = 0

for x in input:
    for i in dial:
        if i[1].count(x):
            result += (i[0] + 1)
            break

print(result)
