def solution(new_id):
    temp = []
    # 1단계
    new_id = new_id.lower()

    # 2단계
    for x in new_id:
        if x.isalpha() or x.isdigit() or x == '-' or x == '_' or x == '.':
            temp.append(x)

    # 3단계
    # id = id.replace("..", ".")
    prev = ''
    string = []
    for x in temp:
        if prev == '.' and x == '.':
            continue
        prev = x
        string.append(x)
    id = ''.join(string)


    # 4단계
    id = id.lstrip('.').rstrip('.')

    # 5단계
    if len(id) == 0:
        id = 'a'

    # 6단계
    if len(id) >= 16:
        id = id[:15]
        id = id.rstrip('.')

    # 7단계
    if len(id) <= 2:
        while len(id) < 3:
            id += id[-1]

    return id


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
