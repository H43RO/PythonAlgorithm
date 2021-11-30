from sys import stdin

vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    case = stdin.readline().strip()

    if case == "end":
        break

    v = False  # 모음 발음 가능 여부
    k = True  # 자음 발음 가능 여부

    for i, x in enumerate(case):
        if x in vowel:
            v = True
        if i > 0:
            if x == case[i - 1] and x != 'e' and x != 'o':  # 3번 조건
                k = False
                break
        if i > 1:
            if x not in vowel:
                if case[i - 1] not in vowel and case[i - 2] not in vowel:
                    k = False
                    break
            if x in vowel:
                if case[i - 1] in vowel and case[i - 2] in vowel:
                    k = False
                    break

    if v and k:
        print("<" + case + "> is acceptable.")
    else:
        print("<" + case + "> is not acceptable.")
