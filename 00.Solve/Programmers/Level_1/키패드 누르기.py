def solution(numbers, hand):
    answer = ''
    keypad = [['1', '4', '7', '*'],
              ['2', '5', '8', '0'],
              ['3', '6', '9', '#']]

    left, right = (0, 3), (2, 3)  # 왼손은 * 에, 오른손은 # 에

    for x in numbers:
        if x == 1 or x == 4 or x == 7:
            answer += 'L'
            left = (0, keypad[0].index(str(x)))
            continue
        elif x == 3 or x == 6 or x == 9:
            answer += 'R'
            right = (2, keypad[2].index(str(x)))
            continue
        else:
            left_distance = abs(keypad[1].index(str(x)) - left[1])
            right_distance = abs(keypad[1].index(str(x)) - right[1])

            if left[0] != 1:
                left_distance += 1
            if right[0] != 1:
                right_distance += 1

            if left_distance > right_distance:
                answer += 'R'
                right = (1, keypad[1].index(str(x)))
                continue
            elif left_distance < right_distance:
                answer += 'L'
                left = (1, keypad[1].index(str(x)))
                continue
            elif left_distance == right_distance:
                if hand == 'left':
                    answer += 'L'
                    left = (1, keypad[1].index(str(x)))
                    continue
                elif hand == 'right':
                    answer += 'R'
                    right = (1, keypad[1].index(str(x)))
                    continue
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))  # LRLLLRLLRRL
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))  # LRLLRRLLLRR
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))  # LLRLLRLLRL