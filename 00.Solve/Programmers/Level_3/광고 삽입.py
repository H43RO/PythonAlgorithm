import heapq


def transform(hour, minute, second):
    return int(hour) * 3600 + int(minute) * 60 + int(second)


def solution(play_time, adv_time, logs):
    # 정수(초 단위) 형태로 영상, 광고 재생 시간 정보를 담고 있음
    hour, minute, second = play_time.split(':')
    play_time = transform(hour, minute, second)

    hour, minute, second = adv_time.split(':')
    adv_time = transform(hour, minute, second)

    total_time = [0] * 360001

    for x in logs:
        start, end = x.split('-')

        # total_time[x] = x 시각에 시작된 재생 구간 개수 - x 시각에 종료된 재생구간 개수
        # - 시작 시각 인덱스를 +1, 종료 시각 인덱스를 -1 해줌으로써 구현
        hour, minute, second = start.split(':')
        start = transform(hour, minute, second)
        total_time[start] += 1

        hour, minute, second = end.split(':')
        end = transform(hour, minute, second)
        total_time[end] -= 1

    # total_time[x] = 시각 x 부터 x + 1 까지 1초 간 구간을 포함하는 재생 구간 개수
    for i in range(1, play_time + 1):
        total_time[i] += total_time[i - 1]
    # total_time[x] = 시각 0 부터 x + 1 까지 x + 1 초 간 구간을 포함하는 누적 재생시간
    for i in range(1, play_time + 1):
        total_time[i] += total_time[i - 1]

    max_sum_time = 0
    max_sum_played = total_time[adv_time]

    # 반복문을 돌며 누적 재생시간이 가장 긴 시간을 max_sum_time 에 넣어줌
    # 마지막으로 업데이트 된 max_sum_time 이 문제에서 요구하는 정답
    for start_time in range(1, play_time):
        end_time = start_time + adv_time if start_time + adv_time < play_time else play_time
        sum_played = total_time[end_time] - total_time[start_time]
        if max_sum_played < sum_played:
            max_sum_played = sum_played
            max_sum_time = start_time + 1

    answer = max_sum_time
    hour = answer // 3600
    answer = answer % 3600
    minute = answer // 60
    answer = answer % 60
    second = answer

    final = ''
    final += str(hour).zfill(2)
    final += ':'
    final += str(minute).zfill(2)
    final += ':'
    final += str(second).zfill(2)

    return final


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]))