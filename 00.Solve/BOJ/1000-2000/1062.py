# from sys import stdin, exit
# from itertools import combinations
#
# # a, n, t, i, c 는 기본적으로 알아야 단어 읽기라도 할 수 있음 (5글자)
# n, k = map(int, stdin.readline().split())
# if k < 5 or k == 26:
#     print(0 if k < 5 else n)
#     exit()
#
# word_set = []
# alpha = []
# limit = k - 5
# for _ in range(n):
#     word = stdin.readline().strip()
#     essential = "antic"
#     word = ''.join(x for x in word if x not in essential)
#     if len(word) <= limit:
#         word_set.append(''.join(sorted(list(set(word)))))
#         for x in word:
#             if x not in alpha:
#                 alpha.append(x)
#
# learned = list(combinations(alpha, limit))
#
# result = []
# for x in learned:
#     count = 0
#     for word in word_set:
#         if len(set(x) | set(word)) <= len(x):
#             count += 1
#     result.append(count)
#
# print(max(result))

from sys import stdin, exit
from itertools import combinations

# 알파벳 각각에 고유 번호 부여
bin_dict = {'b': 20, 'd': 19, 'e': 18, 'f': 17, 'g': 16, 'h': 15, 'j': 14,
            'k': 13, 'l': 12, 'm': 11, 'o': 10, 'p': 9, 'q': 8, 'r': 7,
            's': 6, 'u': 5, 'v': 4, 'w': 3, 'x': 2, 'y': 1, 'z': 0}


# 알파벳 배열을 2진수로 바꾸어주는 함수
def word_to_bin(word):
    answer = 0b0
    for x in word:
        answer = answer | (1 << bin_dict[x])

    return answer


n, k = map(int, stdin.readline().split())
words = []
for _ in range(n):
    words.append(set(stdin.readline().rstrip()[4:-4]).difference('a', 'n', 't', 'i', 'c'))

if k < 5 or k == 26:
    print(0 if k < 5 else n)
    exit()

bin_list = [word_to_bin(x) for x in words]
max_count = 0

# 2^0 부터 2^20 제곱까지 일괄 저장
power_of_2 = []
for i in range(21):
    power_of_2.append(2 ** i)

# k - 5 개의 가르침 받은 알파벳 조합 탐색
for comb in combinations(power_of_2, k - 5):
    current = sum(comb)
    count = 0
    for bin_number in bin_list:
        # 현재 배운 알파벳 조합으로 현재 탐색중인 단어를 읽을 수 있다면
        if bin_number & current == bin_number:
            count += 1
    max_count = max(max_count, count)
print(max_count)
