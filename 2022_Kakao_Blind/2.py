import string

tmp = string.digits + string.ascii_lowercase


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    l = round(n ** 0.5) + 1
    for i in range(3, l, 2):
        if n % i == 0:
            return False
    return True


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def solution(n, k):
    answer = 0
    num = str(convert(n, k))
    data = num.split('0')
    for x in data:
        if x and is_prime(int(x)):
            answer += 1

    return answer


print(solution(437674, 3))
print(solution(110011, 10))
