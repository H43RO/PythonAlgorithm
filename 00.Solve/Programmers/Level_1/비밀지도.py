def solution(n, arr1, arr2):
    answer = []

    data = []
    for x in zip(arr1, arr2):
        temp = list(format(x[0] | x[1], 'b'))
        while len(temp) < n:
            temp.insert(0, '0')
        data.append(temp)

    for x in data:
        temp = ""
        for a in x:
            if a == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
