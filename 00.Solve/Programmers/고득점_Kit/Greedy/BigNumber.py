# 시간 복잡도 초과
# from itertools import combinations

# def solution(number, k):
#     answer = ''
#
#     all_combinations = list(combinations(number, len(number) - k))  # 모든 순열 구하기
#     result = max(all_combinations)
#
#     for x in result:
#         answer += x
#
#     return answer
#
#
# answer = solution("4177252841", 4)
# print(answer)

# 스택 사용
def solution(number, k):
    answer = ''

    arr = [number[0]]

    for num in number[1:]:
        while len(arr) > 0 and arr[-1] < num and k > 0:
            k -= 1
            arr.pop()
        arr.append(num)

    if k != 0:
        list = arr[:-k]

    return answer.join(arr)

print(solution("1234", 2))


# 다른 분 정답 (문자열 슬라이싱 사용)
# def solution(number, k):
#     answer = ''
#     length = len(number)
#
#     if int(number) == 0:
#         answer = '0'
#         return answer
#
#     if length <= k:
#         answer = '0'
#         return answer
#
#     j = 0
#     for x in range(k):
#         for i in range(j, length - 1):
#             if number[i] < number[i + 1]:
#                 number = number[:i] + number[i + 1:]
#                 if i > 0:
#                     j = i - 1
#                 break
#     number = number[:length - k]
#     answer = number
#
#     return answer

