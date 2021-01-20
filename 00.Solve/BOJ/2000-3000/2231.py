num = int(input())

result = 0

i = 0
while True:
    sum = i

    # 문자열로 변환하여 각 자리를 더해줌
    for x in str(i):
        sum += int(x)

    # 만약 최초의 생성자라면
    if sum == num:
        result = i
        break

    # 검사 범위를 넘어서면 중단
    if i > num:
        break

    i += 1

print(result)
