input = input()

result = 0

i = 0
while i < len(input):
    if i + 1 < len(input):
        if input[i] == 'c' and input[i + 1] == '=':
            result += 1
            i += 2
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

        if i + 2 < len(input) and input[i] == 'd' and input[i + 1] == 'z' and input[i + 2] == '=':
            result += 1
            i += 3
            continue

    result += 1
    i += 1

print(result)
