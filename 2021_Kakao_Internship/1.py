dic = {'zero': 0, 'one': 1, 'two': 2,
       'three': 3, 'four': 4, 'five': 5,
       'six': 6, 'seven': 7, 'eight': 8,
       'nine': 9}


def solution(s):
    answer = ''
    temp = ''
    for i, v in enumerate(s):
        if v.isnumeric():
            answer += str(v)
        else:
            temp += v
            if i < len(s) - 1 and s[i + 1].isnumeric():
                answer += str(dic[temp])
                temp = ''
            if temp in dic:
                answer += str(dic[temp])
                temp = ''
    return int(answer)


print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))
