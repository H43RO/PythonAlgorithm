from sys import stdin, stdout


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
        if i >= 2 and prime_list[i] is True and prime_list[n - i] is True and (i + (n - i)) == n:
            stdout.write(f"{n} = {i} + {n - i}\n")
            possible = True
            break
    if possible is False:
        stdout.write("Goldbach's conjecture is wrong.\n")
