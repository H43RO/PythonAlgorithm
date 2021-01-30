from sys import stdin, stdout
import re
from collections import deque

case = int(stdin.readline())
result = []

for i in range(case):
    # 명령어 저장
    operation = list(stdin.readline().strip())
    n = int(stdin.readline())

    # 숫자만 파싱해서 덱에 저장
    numbers = re.findall("\d+", stdin.readline().strip())
    data = deque(list(map(int, numbers)))

    error = False
    reverse = False

    for x in operation:
        if x == 'R':
            reverse = not reverse  # Reverse Flag 반대로 지정
        if x == 'D':
            if data and reverse:  # Reverse Flag 가 참일 때 맨 뒤 요소 제거
                data.pop()
            elif data and not reverse:  # Reverse Flag 거짓일 때 맨 앞 요소 제거
                data.popleft()
            elif not data:  # 데이터가 없다면 Error Flag 발동
                error = True

    # Error Flag 가 발동하지 않았다면 결과 저장
    if error is False:
        # reverse = True 면 역순으로 저장
        if not reverse:
            result.append(data)
        # reverse = False 면 정순으로 저장
        if reverse:
            result.append(reversed(data))
    else:
        result.append("error")

for x in result:
    if x == "error":
        print(x)
    else:
        # 출력 형식 만들기
        result = list("".join(str(list(x))))
        result[0] = "["
        result[-1] = "]"
        result = "".join(result)

        pattern = re.compile(r'\s+')
        result = re.sub(pattern, '', result)

        print(result)
