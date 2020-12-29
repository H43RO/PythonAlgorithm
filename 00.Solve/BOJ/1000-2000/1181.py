n = int(input())

word_list = []

for i in range(n):
    word_list.append(input())

word_list = list(set(word_list))  # 중복 제거
word_list.sort()  # 우선 알파벳 순으로 정렬

word_list.sort(key=lambda x: len(x))  # 이후 길이 순으로 정렬

for x in word_list:
    print(x)