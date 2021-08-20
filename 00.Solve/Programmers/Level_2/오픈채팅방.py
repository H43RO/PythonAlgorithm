def solution(record):
    answer = []
    user = {}
    for x in record:
        if x.startswith("Leave"):
            continue
        cmd, uid, nickname = x.split()
        if cmd == "Enter" or cmd == "Change":
            user[uid] = nickname
    for x in record:
        if x.startswith("Leave"):
            cmd, uid = x.split()
            answer.append(f"{user[uid]}님이 나갔습니다.")
            continue
        cmd, uid, nickname = x.split()
        if cmd == "Enter":
            answer.append(f"{user[uid]}님이 들어왔습니다.")

    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
