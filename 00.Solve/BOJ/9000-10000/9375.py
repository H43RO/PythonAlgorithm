from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    clothes = {}
    n = int(stdin.readline())
    for i in range(n):  # 옷 종류 딕셔너리에 저장
        name, spices = stdin.readline().split()
        if spices in clothes:  # 딕셔너리에 있는 종류라면 개수 1 증가
            clothes[spices] += 1
        else:  # 딕셔너리에 없는 종류라면 종류 추가
            clothes[spices] = 1

    result = 1
    for x in clothes.values():  # 규칙에 의한 공식 적용
        result *= (x + 1)
    print(result - 1)
