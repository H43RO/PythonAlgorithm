from sys import stdin, stdout

T = int(stdin.readline().strip())

for _ in range(T):
    n = int(stdin.readline())

    first = list(map(int, stdin.readline().split()))
    second = list(map(int, stdin.readline().split()))

    # 인덱싱이 헷갈리지 않게 DP 테이블과 인덱스 통일 (맨 앞에 0 삽입)
    first.insert(0, 0)
    second.insert(0, 0)

    dp_first = [0] * (n + 1)
    dp_second = [0] * (n + 1)

    dp_first[1] = first[1]
    dp_second[1] = second[1]

    dp_second[2] = dp_first[1] + second[2]
    dp_first[2] = dp_second[1] + first[2]

    for i in range(3, n + 1):
        dp_first[i] = first[i] + max(dp_second[i - 1], dp_second[i - 2])
        dp_second[i] = second[i] + max(dp_first[i - 1], dp_first[i - 2])

    print(max(dp_first[n], dp_second[n]))
