def solution(name):
    answer = 0
    length = len(name)

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_length = len(alpha)  # 26

    result = ["A"] * length

    i = 0
    while name != ''.join(result):
        if name[i] == 'A':
            answer += 1
            i += 1

        answer += 1

        if alpha.index(name[i]) < 13:  # 위로 가는게 유리
            answer += alpha.index(name[i])
            result[i] = alpha[alpha.index(name[i])]
            if i < length - 1:
                i += 1

        if alpha.index(name[i]) > 13:  # 아래로 가는게 유리
            answer += (alpha_length - alpha.index(name[i]))
            result[i] = alpha[alpha.index(name[i])]
            if i < length - 1:
                i += 1

        if alpha.index(name[i]) == 13:
            answer += alpha.index(name[i])
            result[i] = alpha[alpha.index(name[i])]
            if i < length - 1:
                if name[i + 1] == 'A' and name[i - 1] != 'A':
                    i -= 1
                else:
                    i += 1

        print(i)
        print("".join(result))

    return answer - 1

print(solution("JEROEN"))

# BBBAAAB 9
# ABABAAAAABA 11
# JEROEN 56
# JAN 23
