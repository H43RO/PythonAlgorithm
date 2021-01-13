n = int(input())

list = []

result = 0

for x in range(n):
    list.append(input())

alpha = []

# 추가된 단어들에 대하여 하나씩 탐색
for word in list:
    # 각 단어의 글자 하나 하나를 탐색
    for i, v in enumerate(word):
        # 리스트에 한 글자씩 추가해보면서 매 글자마다 그룹 단어 조건에 부합하는지 확인
        alpha.append(v)

        # 만약 같은 알파벳이 단어 내에서 여러 번 나오는데 연속해있지 않은 경우 그룹 단어가 아님
        if 1 <= i and word[i - 1] != word[i] and alpha.count(word[i]) >= 2:
            break

        # 끝까지 break 조건에 진입하지 않아 그룹 단어인 경우
        if i == len(word) - 1:
            result += 1

    alpha.clear()

print(result)
