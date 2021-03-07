import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville:
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1

        if scoville[0] >= K:
            return answer
        else:
            if len(scoville) <= 1:
                return -1

    return -1


print(solution([1, 2, 3, 9, 10, 12], 7))
