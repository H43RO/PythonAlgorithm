def solution(s):
    answer = []
    temp = s.lstrip('{').rstrip('}').split('},{')
    data = []
    [data.append(x) for x in temp]
    data.sort(key=lambda x: len(x))
    for x in data:
        temp = x.split(',')
        for a in temp:
            if int(a) not in answer:
                answer.append(int(a))
                continue

    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
