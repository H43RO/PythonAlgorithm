def check(data, left, right):
    count = 0
    for x in data:
        if x[1] < left or x[0] >= right:
            continue
        if (x[0] <= left and x[1] <= right) or (x[0] <= left and right <= x[1]) or (x[0] >= left and x[1] <= right) \
                or (x[0] >= left and x[1] >= right):
            count += 1
    return count


def solution(lines):
    answer = 0
    data = []
    for i, x in enumerate(lines):
        _, end_time, process = x.split()
        process = float(process[:-1])
        hour, minute, second = end_time.split(':')
        end = int((float(hour) * 3600 + float(minute) * 60 + float(second)) * 1000)
        start = int(end - (process * 1000) + 1)
        data.append((start, end))

    for a in data:
        result = max(check(data, a[0], a[0] + 1000), check(data, a[1], a[1] + 1000))
        answer = max(answer, result)

    if answer == 0:
        answer = 1
    return answer


print(solution(["2016-09-15 00:00:00.000 3s"]))
print(solution(["2016-09-15 23:59:59.999 0.001s"]))
print(solution([
    "2016-09-15 01:00:04.001 2.0s",
    "2016-09-15 01:00:07.000 2s"
]))

print(solution([
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
]))

print(solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]))
print(solution(["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]))
