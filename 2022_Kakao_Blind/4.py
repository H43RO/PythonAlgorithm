import copy
import sys

sys.setrecursionlimit(10000000)

info = []
answer = []
visited = []


def check(n, i, count):
    if i > n or sum(count) > n:
        return
    if sum(count) == n:
        apeach, lion = 0, 0
        for i in range(11):
            a, b = info[i], count[i]
            if a == b == 0:
                continue
            if a >= b:
                apeach += (10 - i)
            else:
                lion += (10 - i)
        if apeach < lion:
            if answer and answer[0][0] < lion:
                answer.clear()
            if answer and answer[0][0] > lion:
                return
            answer.append((lion, count))
        return

    # 가지치기
    if i < n:
        for j in range(11):
            temp = copy.deepcopy(count)
            temp[j] += 1
            if temp in visited:
                continue
            visited.append(temp)
            check(n, i + 1, temp)
            check(n, i - 1, temp)


def solution(n, data):
    global info
    info = data
    answer.clear()
    visited.clear()

    check(n, 0, info)

    if not answer:
        return [-1]
    answer.sort(key=lambda x: ''.join(str(reversed(x[1]))), reverse=True)
    return answer[0][1]


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
