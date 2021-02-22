from itertools import permutations
import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    nums = []

    for i in range(1, len(numbers) + 1):
        for x in list(permutations(numbers, i)):
            nums.append(int("".join(x)))

    nums = sorted(list(set(nums)))

    for x in nums:
        if is_prime(x):
            answer += 1

    return answer


print(solution(numbers="011"))
