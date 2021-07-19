from sys import stdin

a, p = map(int, stdin.readline().split())
sequence = [a]  # D[1] = A

while True:
    num = str(sequence[-1])  # 현재 수열 마지막 숫자
    temp = 0
    for x in num:  # D[n] = D[n-1]의 각 자리의 숫자를 P번 곱한 수들의 합
        temp += int(x) ** p
    if temp in sequence:  # D[n] 이 만약 현재 수열에 존재한다면
        print(sequence.index(temp))  # 그 인덱스가 반복 수열 제외 개수
        break
    sequence.append(temp)  # 등장하지 않는다면 수열에 추가
