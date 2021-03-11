def solution(A, B):
    answer = 0

    A.sort()
    B.sort()

    for i in range(len(A)):
        for j in range(len(B)):
            if B[j] > A[i]:
                answer += 1
                del B[j]
                break

    return answer


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))