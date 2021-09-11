def solution(id_list, report, k):
    answer = []
    data = {}
    for x in id_list:
        data[x] = [0, []]
    for x in report:
        user, report_user = x.split()
        if report_user not in data[user][1]:
            data[report_user][0] += 1
            data[user][1].append(report_user)

    for x in data:
        temp = 0
        for a in data[x][1]:
            if data[a][0] >= k:
                temp += 1
        answer.append(temp)

    return answer


print(
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
             2))
