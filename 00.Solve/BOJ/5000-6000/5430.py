"""
 1. 시간초과
    - 큰 데이터에 대하여 reverse() 를 사용하게 되면 엄청난 연산을 하게 될 수 있다는 것을 간과했다.
      Flag 변수를 두어 pop() 위치를 조정하는 방식 (앞에서 pop() 할지, 뒤에서 pop() 할지) 으로 변경하였다.

 2. 틀렸습니다
    - 코드 상 문제가 없어보이는데 계속 틀렸다고 나오는 것을 보고 한참 고민하다가
      출력 형식이 잘못된 것을 깨닫고 다시 돌렸더니 정답 처리 되었다.
      다음부턴 공백 문자 등의 유무 등 출력 형식을조심해야겠다.
"""

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
