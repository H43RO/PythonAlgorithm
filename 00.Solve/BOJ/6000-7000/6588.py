from sys import stdin, stdout


# True, False 값으로 인덱싱할 수 있도록
# 에라토스테네스를 활용하여 소수 판별 리스트 생성
def prime(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] is True:
            for j in range(i + i, n, i):
                sieve[j] = False

    return sieve


prime_list = prime(1000000)

while True:
    n = int(stdin.readline())
    if n == 0:
        break

    possible = False
    for i, v in enumerate(prime_list):
        # i, n - i 이 모두 소수이고 골드바흐의 추측 조건에 성립할 때
        if i >= 2 and prime_list[i] is True and prime_list[n - i] is True and (i + (n - i)) == n:
            stdout.write(f"{n} = {i} + {n - i}\n")
            possible = True
            break
    if possible is False:
        stdout.write("Goldbach's conjecture is wrong.\n")
