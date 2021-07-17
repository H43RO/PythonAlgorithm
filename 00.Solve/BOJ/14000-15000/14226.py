from sys import stdin
from collections import deque

s = int(stdin.readline())
visited = dict()
visited[(1, 0)] = 0

queue = deque([(1, 0)])
while queue:
    sticker, clipboard = queue.popleft()
    if sticker == s:
        print(visited[(sticker, clipboard)])
        break

    if (sticker, sticker) not in visited.keys():  # 모두 클립보드 저장
        visited[(sticker, sticker)] = visited[(sticker, clipboard)] + 1
        queue.append((sticker, sticker))

    if (sticker + clipboard, clipboard) not in visited.keys():  # 클립보드 내용 모두 붙여넣기
        visited[(sticker + clipboard, clipboard)] = visited[(sticker, clipboard)] + 1
        queue.append((sticker + clipboard, clipboard))

    if (sticker - 1, clipboard) not in visited.keys():  # 이모티콘 1개 삭제
        visited[(sticker - 1, clipboard)] = visited[(sticker, clipboard)] + 1
        queue.append((sticker - 1, clipboard))
