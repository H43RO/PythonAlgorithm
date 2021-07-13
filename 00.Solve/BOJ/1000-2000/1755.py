from sys import stdin

num = {
    0: "zero", 1: "one", 2: "two", 3: "three",
    4: "four", 5: "five", 6: "six", 7: "seven",
    8: "eight", 9: "nine"
}

M, N = map(int, stdin.readline().split())
data = []

for i in range(M, N + 1):
    temp = ""
    for x in str(i):  # 숫자 자릿수 하나하나 탐색
        temp += num[int(x)]  # 매핑되는 문자열 추가해줌
    data.append((temp, i))  # 완성된 문자열과 원래 숫자 같이 저장
data.sort()  # 파이썬은 문자열 들에 대한 sort() 가 기본적으로 사전순 정렬을 지원함

for i in range(len(data)):
    if i % 10 == 0 and i != 0:  # 10개씩 끊어 출력
        print()
    print(data[i][1], end=' ')  # 원래 숫자 (정수형) 출력
