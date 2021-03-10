from collections import deque

def solution(numbers, target):
    answer = 0

    queue = deque()
    queue.append((0, 0))  # sum, level

    while queue:
        sum, level = queue.popleft()
        if level > len(numbers):
            break
        if level == len(numbers) and sum == target:
            answer += 1
        queue.append((sum + numbers[level - 1], level + 1))
        queue.append((sum - numbers[level - 1], level + 1))

    return answer


print(solution([1, 1, 1, 1, 1], 3))