def solution(N, number):
    possible = [0, [N]]
    if N == number:
        return 1
    for i in range(2, 9):
        case = []
        basic_num = int(str(N) * i)  # 55, 555 등
        case.append(basic_num)
        for j in range(1, i // 2 + 1):
            for x in possible[j]:
                for y in possible[i - j]:
                    case.append(x + y)
                    case.append(x - y)
                    case.append(y - x)
                    case.append(x * y)
                    if y != 0:
                        case.append(x / y)
                    if x != 0:
                        case.append(y / x)
            if number in case:
                return i
            possible.append(case)
    return -1