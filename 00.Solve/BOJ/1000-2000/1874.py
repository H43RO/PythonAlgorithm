from sys import stdin, stdout

n = int(stdin.readline())

data = []
stack = []
result = []
index = 0

for i in range(n):
    data.append(int(stdin.readline()))

i = 0
while True:
    # 입력된 숫자만큼 반복했을 때 stack 이 클리어 되었다면 수열 재현 성공
    if i > n and len(stack) == 0:
        break

    # 더 반복해보는데도 stack 이 클리어 되지 않는다면 수열 재현 불가
    if i > n * 2 and len(stack) != 0:
        result.clear()
        result.append("NO")
        break

    # stack 의 최상단이 수열 구현에 필요한 숫자일 경우 pop
    if len(stack) != 0 and stack[len(stack) - 1] == data[index]:
        stack.pop()
        index += 1
        operation = "-"
        result.append(operation)
        continue

    # n 범위 내에서는 매 루프마다 오름차순으로 차례대로 push 하게됨
    if i in range(1, n + 1):
        stack.append(i)
        operation = "+"
        result.append(operation)

    i += 1

for x in result:
    print(x)
