from sys import stdin, stdout

# n = int(stdin.readline())
#
# stack = list(map(int, stdin.readline().split()))
# deleted = []
# result = []
#
# for i in range(n):
#     standard = stack.pop()
#     no_answer = True
#
#     while stack:
#         x = stack.pop()
#         deleted.append(x)
#
#         if standard < x:
#             result.append(len(stack) + 1)
#             no_answer = False
#             break
#
#     if no_answer:
#         result.append(0)
#
#     while deleted:
#         stack.append(deleted.pop())
#
#
# while result:
#     stdout.write(str(result.pop()) + " ")

n = int(stdin.readline())
top_list = list(map(int, stdin.readline().split()))
stack = [(1, top_list[0])]  # 맨 처음 원소는 첫 탑
result = [0]  # 맨 앞 결과는 무조건 0

for i in range(1, n):
    while stack:
        if top_list[i] < stack[-1][1]:
            result.append(stack[-1][0])
            break
        else:
            stack.pop()
    if not stack:
        result.append(0)
    stack.append((i + 1, top_list[i]))

for x in result:
    print(x, end=' ')
