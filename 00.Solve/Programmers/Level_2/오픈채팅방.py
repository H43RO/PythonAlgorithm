def solution(record):
    answer = []
    user = {}
    # 최종 닉네임이 저장될 때 까지 갱신
    for x in record:
        if x.startswith("Leave"):  # 톡방 나가는거 노상관
            continue
        cmd, uid, nickname = x.split()
        user[uid] = nickname

    # 최종 닉네임을 활용하여 기록대로 출력
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

# 2019 카카오 블라인드 채용 1번 문제
# 정답률 : 59.91%
# - 7분 소요
