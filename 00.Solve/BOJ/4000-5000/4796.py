from sys import stdin, stdout

i = 1

while True:
    result = 0
    # 연속하는 P 일 중 L 일 동안 사용할 수 있고, 휴가는 V 일 짜리임
    L, P, V = map(int, stdin.readline().split())

    if L == 0 and P == 0 and V == 0:
        break

    # 휴가를 다 쓸 때까지
    while V > 0:
        # V 가 L 보다 작으면 V 만큼 더해줌 (남은 휴가 일수가 있다면 몰빵)
        if V < L:
            result += V
        # V 가 L 보다 크거나 같으면 L 만큼 더해줌 (채울 수 있는대로 꽉 채움)
        else:
            result += L
        # 매 루프마다 V 를 P 만큼 빼줌 (휴가 간격 유지)
        V -= P

    print(f"Case {i}: {result}")
    i += 1
