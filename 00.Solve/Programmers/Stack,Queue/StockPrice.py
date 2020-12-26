"""
 Queue 자료구조를 활용하여 풀어보았다. 큐의 첫 번째 원소를 계속 Pop 하여
 Pop 한 원소 이후의 모든 원소를 탐색하면서 가격이 떨어지기까지의 기간을 계산함
 * 가독성을 챙기는 대신 O(N^2) 의 복잡도를 가지게 됨
"""

from collections import deque


def solution(prices):
    queue = deque(prices)
    answer = []
    while queue:
        price = queue.popleft()
        period = 0

        if len(queue) == 0:
            answer.append(0)
            break

        for i, v in enumerate(queue):
            period += 1

            if v < price:
                answer.append(period)
                period = 0
                break

            if i == len(queue) - 1:
                answer.append(period)
                period = 0

    return answer


print(solution([1, 2, 3, 2, 3]))
