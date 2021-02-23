def solution(citations):
    answer = 0

    for i in range(max(citations) + 1):
        temp = [x for x in citations if x >= i]
        if i <= len(temp):
            answer = i

    return answer


print(solution([3, 0, 6, 1, 5]))  # 3
print(solution([12, 11, 10, 9, 8, 1]))  # 5
print(solution([6, 6, 6, 6, 6, 1]))  # 5
print(solution([4, 4, 4]))  # 3
print(solution([4, 4, 4, 5, 0, 1, 2, 3]))  # 4
print(solution([10, 11, 12, 13]))  # 4
print(solution([0, 0, 1, 1]))  # 1
print(solution([0, 1]))  # 1
print(solution([10, 9, 4, 1, 1]))  # 3
