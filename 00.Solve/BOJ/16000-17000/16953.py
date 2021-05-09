a, b = map(int, input().split())
count = 0

# B 를 A 로 바꾸는 방식의 로직
while b > a:
    count += 1

    # 만약 1로 끝나는 숫자라면 맨 뒷자리 제거
    if str(b).endswith('1'):
        b = int(str(b)[:-1])
    # 만약 2로 나누어 떨어지는 숫자라면 2로 나눔
    elif b % 2 == 0:
        b = b // 2
    # 2가지 경우의 수에 모두 해당 안되면 구제불능
    else:
        break

if b == a:
    print(count + 1)
else:
    print(-1)