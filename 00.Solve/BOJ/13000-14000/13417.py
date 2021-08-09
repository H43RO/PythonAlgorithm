from sys import stdin
from collections import deque

T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())
    data = deque(list(stdin.readline().strip().split()))
    card = deque([])
    while data:
        x = data.popleft()
        if not card:
            card.append(x)
            continue
        if card[0] >= x:
            card.appendleft(x)
        else:
            card.append(x)

    print(''.join(card))
