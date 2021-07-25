from sys import stdin

s = list(stdin.readline().strip())
word = []

# 단어의 시작과 끝 찾기
is_tag = False
is_word = False
start = 0
for i, v in enumerate(s):
    if v == '>':  # 태그 종료 시 플래그 비활성화
        is_tag = False
        continue
    if is_tag:  # 태그 내부 문자열 무시
        continue
    if v == '<':  # 태그 시작 시 플래그 활성화
        is_tag = True
        if is_word:
            word.append((start, i))
            is_word = False
        continue
    if v == ' ':  # 한 단어가 완성되면
        word.append((start, i))
        is_word = False
        continue
    if is_word:
        continue
    if v.isalpha() or v.isdigit():
        start = i
        is_word = True
        continue

if is_word:
    word.append((start, len(s)))

for x in word:
    start, end = x[0], x[1]
    s = s[:start] + list(reversed(s[start:end])) + s[end:]

print(''.join(s))