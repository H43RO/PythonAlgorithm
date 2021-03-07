def solution(num):
    num = list(map(str, num))
    num.sort(key=lambda x: x * 3, reverse=True)
    print(num)

    return str(int(''.join(num)))


print(solution([3, 30, 34, 5, 9]))
