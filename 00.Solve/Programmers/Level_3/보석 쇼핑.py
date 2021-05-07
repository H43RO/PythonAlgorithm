def solution(gems):
    n = len(set(gems))
    result = [0, len(gems) - 1]
    left = 0
    right = 0
    dic = {gems[0]: 1}
    while left < len(gems) and right < len(gems):
        if len(dic) == n:
            if result[1] - result[0] > right - left:
                result[0] = left
                result[1] = right
            if dic[gems[left]] == 1:
                del dic[gems[left]]
            else:
                dic[gems[left]] -= 1
            left += 1
        else:
            right += 1
            if right == len(gems):
                break
            else:
                if dic.get(gems[right]) is None:
                    dic[gems[right]] = 1
                else:
                    dic[gems[right]] += 1
    result[0] += 1
    result[1] += 1
    return result


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
