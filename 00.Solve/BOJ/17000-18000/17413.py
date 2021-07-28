from sys import stdin

s = list(stdin.readline().strip())
word = []

is_tag = False  # 현재 태그 내부에 있는지에 대한 플래그
is_word = False  # 현재 단어 내부에 있는지에 대한 플래그

start = 0
for i, v in enumerate(s):
    if v == '>':  # 태그 종료 시 태그 플래그 비활성화
        is_tag = False
        continue
    if is_tag:  # 태그 내부의 문자열의 경우 패스
        continue
    if v == '<':  # 태그 시작 시 태그 플래그 활성화
        is_tag = True
        if is_word:  # 만약 이전까지 한 단어였다면
            word.append((start, i))  # 해당 단어의 처음과 끝 인덱스 저장 후
            is_word = False  # 단어 플래그 비활성화
        continue
    if v == ' ':  # 한 단어가 완성되면
        word.append((start, i))  # 해당 단어의 처음과 끝 인덱스 저장 후
        is_word = False  # 단어 플래그 비활성화
        continue
    if is_word:  # 단어 내부의 문자열의 경우 패스
        continue
    # 위 조건문 각각에 continue 가 달려있으므로
    # 만약 단어를 처음 만나는 경우 아래 조건문에 분기됨
    if v.isalpha() or v.isdigit():
        start = i  # 단어 시작점을 저장해두고
        is_word = True  # 단어 플래그 활성화
        continue

if is_word:  # 루프가 끝난 뒤 처리되지 않은 단어까지 처리
    word.append((start, len(s)))

for x in word:  # 저장해둔 단어의 (처음, 끝) 인덱스 각각에 대하여 reversed 처리
    start, end = x[0], x[1]
    s = s[:start] + list(reversed(s[start:end])) + s[end:]

print(''.join(s))
