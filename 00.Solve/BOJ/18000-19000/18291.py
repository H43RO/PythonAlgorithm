from sys import stdin

MOD = 1_000_000_007
T = int(stdin.readline())

for _ in range(T):
    # 규칙에 따라 2의 (N - 2) 제곱이 정답임
    n = int(stdin.readline())
    if n == 1 or n == 2:
        print(1)
        continue
    n -= 2
    form = []
    while True:
        if n == 1:
            break
        if n % 2 == 0:
            form.append(False)
        else:
            form.append(True)
        n = n // 2

    d = 2
    result = d

    for x in form[::-1]:
        if x:
            result = result ** 2 * d
        else:
            result = result ** 2
        result = result % MOD

    print(result)

# 예? pow() 함수로도 풀린다구요..?
# ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
