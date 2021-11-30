from sys import stdin

vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    case = stdin.readline().strip()

    if case == "end":
        break

    v = False  # 모음 포함 여부
    available = True  # 조건 충족 여부

    for i, x in enumerate(case):
        if x in vowel:  # 모음 한 글자라도 있으면 v 활성화
            v = True
        if i > 0:
            # 같은 글자가 연속 두 번 나올 경우 (단 ee, oo 는 허용)
            if x == case[i - 1] and x != 'e' and x != 'o':
                available = False  # 조건 불충족
                break
        if i > 1:
            if x not in vowel:  # 자음이 연속 세 번 나오는지 검사
                if case[i - 1] not in vowel and case[i - 2] not in vowel:
                    available = False
                    break
            if x in vowel:  # 모음이 연속 세 번 나오는지 검사
                if case[i - 1] in vowel and case[i - 2] in vowel:
                    available = False
                    break

    if v and available:
        print("<" + case + "> is acceptable.")
    else:
        print("<" + case + "> is not acceptable.")
