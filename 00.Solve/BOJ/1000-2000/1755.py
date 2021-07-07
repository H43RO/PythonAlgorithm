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
        temp += num[int(x)]
        temp += " "
    data.append((temp, i))
data.sort()

for i in range(len(data)):
    if i % 10 == 0 and i != 0:
        print()
    print(data[i][1], end=' ')
