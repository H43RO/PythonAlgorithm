def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수 호출')
    recursive_function(i + 1)
    print(i, '번째 재귀함수 종료')


recursive_function(1)


def factorial_recursive(n):
    if n <= 1:  # n 이 1 이하인 경우 1 반환
        return 1
    # n! = n * (n - 1)! 을 코드로 작성
    return n * factorial_recursive(n - 1)


print(factorial_recursive(5))


# 유클리드 호제법
# - 두 자연수 A, B 에 대하여 A 를 B 로 나눈 나머지를 R 이라고 할 때,
#   A, B 의 최대공약수는 B 와 R 의 최대 공약수와 같다는 수학적 성질

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print(gcd(192, 162))
