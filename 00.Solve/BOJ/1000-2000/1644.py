from sys import stdin, stdout


def prime(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]


n = int(stdin.readline())
prime_list = prime(n + 1)

result = 0
sum = 0
end = 0

for start in range(len(prime_list)):
    while sum < n and end < len(prime_list):
        sum += prime_list[end]
        end += 1
    if sum == n:
        result += 1
    sum -= prime_list[start]

print(result)
