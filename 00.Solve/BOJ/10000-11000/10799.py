from sys import stdin, stdout

data = list(stdin.readline().strip())
stack = []
result = 0

for i, v in enumerate(data):
    # 만약 레이저를 만난 상황이라면 Stack 에 남아있는 막대기 개수 만큼
    # 결과값 증가 (레이저에 의해 막대기들이 잘리기 때문)
    if data[i - 1] == "(" and v == ")":
        stack.pop()  # '(' 이지만 결국 레이저이기 때문에 pop()
        result += len(stack)
    # 일단 무조건 '(' 를 만나면 Stack 에 push() 함
    elif v == "(":
        stack.append(v)
    # 만약 ")" 를 만나면 (레이저가 아닌 경우)
    # 어떤 한 쇠막대기의 절단되고 남은 부분이 나오므로 결과값 1 증가
    elif v == ")":
        stack.pop()  # 쇠막대기 앞 부분 pop()
        result += 1

print(result)
