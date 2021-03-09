def solution(dirs):
    answer = 0

    visited = []
    x, y = 5, 5

    for c in dirs:
        start_x, start_y = x, y

        if c == 'U':
            x -= 1
            if not 0 <= x < 11:
                x += 1
                continue
        elif c == 'D':
            x += 1
            if not 0 <= x < 11:
                x -= 1
                continue
        elif c == 'R':
            y += 1
            if not 0 <= y < 11:
                y -= 1
                continue
        elif c == 'L':
            y -= 1
            if not 0 <= y < 11:
                y += 1
                continue

        if ((start_x, start_y), (x, y)) in visited:
            continue
        else:
            visited.append(((start_x, start_y), (x, y)))
            visited.append(((x, y), (start_x, start_y)))
            answer += 1

    return answer


print(solution("LULLLLLLU"))
