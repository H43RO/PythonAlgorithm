def solution(str1, str2):
    list_str1 = []
    list_str2 = []

    for s1, slice_s1 in zip(str1, str1[1:]):
        join_str = ''.join(s1 + slice_s1)
        if join_str.isalpha():
            list_str1.append(join_str.lower())

    for s2, slice_s2 in zip(str2, str2[1:]):
        join_str = ''.join(s2 + slice_s2)
        if join_str.isalpha():
            list_str2.append(join_str.lower())

    if len(list_str1) > len(list_str2):
        inter = [list_str1.remove(x) for x in list_str2 if x in list_str1 ]
    else:
        inter = [list_str2.remove(x) for x in list_str1 if x in list_str2 ]

    list_uni = list_str1 + list_str2

    if len(list_uni) == 0:
        return 65536

    return int(len(inter) / len(list_uni) * 65536)


print(solution('FRANCE', 'french'))
