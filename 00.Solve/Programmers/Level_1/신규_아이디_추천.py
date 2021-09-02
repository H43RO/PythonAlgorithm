def solution(new_id):
    temp = []
    # 1단계 - 모든 대문자를 소문자로 치환
    new_id = new_id.lower()

    # 2단계 - 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표 제외 모두 제거
    for x in new_id:
        if x.isalpha() or x.isdigit() or x == '-' or x == '_' or x == '.':
            temp.append(x)

    # 3단계 - 마침표 2번 이상 연속된 부분 마침표 1개로 치환
    id = ''.join(temp)
    while '..' in id:
        id = id.replace('..', '.')

    # 4단계 - 마침표가 처음이나 끝에 있다면 제거
    id = id.lstrip('.').rstrip('.')

    # 5단계 - 빈 문자열이라면 "a" 대입
    if len(id) == 0:
        id = 'a'

    # 6단계 - 길이가 16자 이상이라면, 첫 15개 제외 나머지 모두 제거
    #       - 만약 제거 후 마침표가 끝에 위치한다면 제거
    if len(id) >= 16:
        id = id[:15]
        id = id.rstrip('.')

    # 7단계 - 길이가 2자 이하라면 마지막 문자를 길이가 3이 될 때까지 반복해서 붙임
    if len(id) <= 2:
        while len(id) < 3:
            id += id[-1]

    return id


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))

# 2021년 카카오 블라인드 공채 1번
# 정답률 : 57.50%
# - 4분 40초 소요
