from sys import stdin, stdout
import re
from collections import deque

case = int(stdin.readline())
result = []

for i in range(case):
    operation = list(stdin.readline().strip())
    n = int(stdin.readline())
    numbers = re.findall("\d+", stdin.readline().strip())
    data = deque(list(map(int, numbers)))

    error = False
    reverse = False

    for x in operation:
        if x == 'R':
            reverse = not reverse  # reverse Flag 반대로
        if x == 'D':
            if data and reverse:  # reverse Flag 참일 때 맨 뒤 요소 제거
                data.pop()
            elif data and not reverse:  # reverse Flag 거짓일 때 맨 앞 요소 제거
                data.popleft()
            elif not data:
                error = True

    if error is False:
        # reverse = True 면 역순으로 저장
        # reverse = False 면 정순으로 저장
        if not reverse:
            result.append(data)
        if reverse:
            result.append(reversed(data))
    else:
        result.append("error")

for x in result:
    if x == "error":
        print(x)
    else:
        result = list("".join(str(list(x))))
        result[0] = "["
        result[-1] = "]"
        result = "".join(result)

        pattern = re.compile(r'\s+')
        result = re.sub(pattern, '', result)

        print(result)
