from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
# 번호에 따른 포켓몬 이름을 저장하는 리스트
name = [0]
# 이름에 따른 번호를 저장하는 리스트
number = {}

for i in range(1, n + 1):
    temp = stdin.readline().strip()
    name.append(temp)
    number[temp] = i

for _ in range(m):
    problem = stdin.readline().strip()
    if problem.isalpha():
        print(number[problem])
    elif problem.isdigit():
        print(name[int(problem)])
