from collections import deque
import heapq


def solution(n, k, cmd):
    answer = ['O'] * n
    queue = list(range(0, n))

    left = []
    for x in queue[:k]:
        heapq.heappush(left, (-x, x))

    # 커서는 Right 힙의 최상위 원소라고 둠
    right = queue[k:]
    heapq.heapify(right)

    # 스택 형태로 '최근 지운 목록' 관리
    deleted = []

    for op in cmd:
        # 커서를 위로 이동할 때
        if op[0] == 'U':
            temp = op.split()
            for i in range(int(temp[1])):
                heapq.heappush(right, heapq.heappop(left)[1])
        # 커서를 아래로 이동할 때
        if op[0] == 'D':
            temp = op.split()
            for i in range(int(temp[1])):
                num = heapq.heappop(right)
                heapq.heappush(left, (-num, num))
        # 커서 원소를 삭제할 때
        if op[0] == 'C':
            heapq.heappush(deleted, (-(len(deleted) + 1), heapq.heappop(right)))
            if not right:
                heapq.heappush(right, heapq.heappop(left)[1])
        # 최근에 삭제한 원소를 복구할 때
        if op[0] == 'Z':
            restored = heapq.heappop(deleted)[1]
            if restored < right[0]:
                heapq.heappush(left, (-restored, restored))
            else:
                heapq.heappush(right, restored)

    while deleted:
        index = heapq.heappop(deleted)[1]
        answer[index] = 'X'

    return ''.join(answer)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
