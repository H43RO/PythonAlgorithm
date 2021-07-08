from sys import stdin

count = 1
while True:
    result = 0
    data = stdin.readline().strip()
    if data.startswith('-'):
        break
    stack = []
    for x in data:
        if len(stack) > 0 and stack[-1] == '{' and x == '}':
            stack.pop()
            continue
        stack.append(x)
    while stack:
        a = stack.pop()
        b = stack.pop()
        if a == b:
            result += 1
        else:
            result += 2
    print(f'{count}. {result}')

    count += 1
