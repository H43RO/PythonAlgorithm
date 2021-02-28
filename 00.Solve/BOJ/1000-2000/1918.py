from sys import stdin, stdout

exp = list(stdin.readline().strip())

stack = []

for x in exp:
    if x == '+' or x == '-':
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')
        stack.append(x)
    elif x == '*' or x == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            print(stack.pop(), end='')
        stack.append(x)
    elif x == '(':
        stack.append(x)
    # '(' 만날 때 까지 pop()
    elif x == ')':
        while True:
            if stack[-1] == '(':
                stack.pop()
                break
            print(stack.pop(), end='')
    else:
        print(x, end='')

while stack:
    print(stack.pop(), end='')
