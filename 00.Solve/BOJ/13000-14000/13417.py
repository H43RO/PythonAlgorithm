from sys import stdin
from collections import deque

T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())
    data = deque(list(stdin.readline().strip().split()))
    card = deque([data.popleft()])  # 첫 문자 무조건 삽입
    while data:
        x = data.popleft()
        if card[0] >= x:  # 카드 맨 앞 글자보다 이전 순위 알파벳 들어오면
            card.appendleft(x)  # 카드 맨 앞에 추가
        else:  # 후순위 알파벳이라면 카드 맨 뒤에 추가
            card.append(x)

    print(''.join(card))
