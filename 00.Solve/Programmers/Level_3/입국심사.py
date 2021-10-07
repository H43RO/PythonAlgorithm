def solution(n, times):
    start = 1
    end = times[-1] * n

    while start <= end:
        mid = (start + end) // 2

        temp = 0
        for x in times:
            temp += mid // x

        if temp >= n:
            end = mid - 1
            result = mid
        else:
            start = mid + 1

    return result


print(solution(6, [7, 10]))
