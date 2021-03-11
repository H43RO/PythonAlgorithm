import heapq


def transform(hour, minute, second):
    return int(hour) * 3600 + int(minute) * 60 + int(second)


def solution(play_time, adv_time, logs):
    q = []

    # 정수 형태로 영상, 광고 재생 시간 정보를 담고 있음
    hour, minute, second = play_time.split(':')
    play_time = transform(hour, minute, second)

    hour, minute, second = adv_time.split(':')
    adv_time = transform(hour, minute, second)

    if play_time == adv_time:
        return "00:00:00"

    for x in logs:
        start, end = x.split('-')

        hour, minute, second = start.split(':')
        start = transform(hour, minute, second)
        hour, minute, second = end.split(':')
        end = transform(hour, minute, second)

        # 힙에 재생 시작 시간, 종료 시간, 총 재생 시간에 대하여 기록
        q.append((start, end))

    # 재생 시작 시간 순으로 정렬
    q.sort()

    result = []
    for i in range(len(q)):
        # 재생 시작 시간 + 광고 길이 를 기준으로 봤을 때
        start = q[i][0]
        end = adv_time + q[i][0]
        count = 0
        for j in range(len(q)):
            if (q[j][0] <= end or q[j][1] <= end) or (start <= q[j][0] <= end):
                count += 1
            if q[j][1] < start:
                break
        result.append(count)

    answer = result.index(max(result))
    answer = q[answer][0]

    hour = answer // 3600
    answer = answer % 3600
    minute = answer // 60
    answer = answer % 60
    second = answer

    final = ''
    if hour < 10:
        final += '0'
        final += str(hour)
    else:
        final += str(hour)

    final += ':'

    if minute < 10:
        final += '0'
        final += str(minute)
    else:
        final += str(minute)

    final += ':'

    if second < 10:
        final += '0'
        final += str(second)
    else:
        final += str(second)

    return final


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]))