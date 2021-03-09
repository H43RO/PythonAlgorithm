def solution(files):
    answer = []
    for x in files:
        head, number, tail = '', '', ''
        temp = 0
        for i in range(len(x)):
            if x[i].isdecimal():
                temp = i
                break
            head += x[i]
        for i in range(temp, len(x)):
            if not x[i].isdecimal():
                temp = i
                break
            number += x[i]
        tail += x[temp:]

        answer.append((head.lower(), number, tail, x))
        answer.sort(key=lambda x: (x[0], int(x[1])))
    answer.sort(key=lambda x: (x[0], int(x[1])))

    result = []
    for x in answer:
        result.append(x[3])

    return result


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))