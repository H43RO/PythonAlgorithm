from sys import stdin

data = list(stdin.readline().strip())
value = {')': 2, ']': 3}  # 괄호값 딕셔너리
stack = []

for x in data:
    temp = 0
    if x == ")" or x == "]":  # 닫는 괄호를 만나면
        while stack:  # 최대 : 스택이 비어있을 때 까지
            top = stack.pop()  # 우선 스택에서 팝한 값을 놓고 봤을 때
            if (top == "(" and x == ')') or (top == '[' and x == ']'):  # 쌍 맞는 괄호의 경우
                stack.append(value[x] if temp == 0 else value[x] * temp)  # 해당 괄호값 * temp 값 stack 에 푸시
                break
            elif top == "(" or top == '[':  # 쌍이 안 맞는 경우 즉시 프로그램 종료
                print("0")
                exit(0)
            else:  # 숫자인 경우 temp 값에 더해줌
                temp += top
        continue
    stack.append(x)  # 닫는 괄호 빼고 나머지는 모두 stack 에 푸시

print(0 if '(' in stack or '[' in stack else sum(stack))
