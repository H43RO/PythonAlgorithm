input = input()

result = 0

i = 0  # 처음부터 차례대로 완전 탐색
while i < len(input):
    if i + 1 < len(input):
        # 크로아티아 알파벳 케이스 8개 정의
        if input[i] == 'c' and input[i + 1] == '=':
            result += 1
            i += 2  # 알파벳 길이만큼 인덱스 증가
            continue
        elif input[i] == 'c' and input[i + 1] == '-':
            result += 1
            i += 2
            continue
        elif input[i] == 'd' and input[i + 1] == '-':
            result += 1
            i += 2
            continue
        elif input[i] == 'l' and input[i + 1] == 'j':
            result += 1
            i += 2
            continue
        elif input[i] == 'n' and input[i + 1] == 'j':
            result += 1
            i += 2
            continue
        elif input[i] == 's' and input[i + 1] == '=':
            result += 1
            i += 2
            continue
        elif input[i] == 'z' and input[i + 1] == '=':
            result += 1
            i += 2
            continue

        elif i + 2 < len(input) and input[i] == 'd' and input[i + 1] == 'z' and input[i + 2] == '=':
            result += 1
            i += 3
            continue

    # 일반 알파벳일 경우
    result += 1
    i += 1

print(result)
