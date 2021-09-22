import math


def solution(fees, records):
    answer = []

    park = {}
    total = {}  # Key : 자동차 번호, Value : 누적 시간
    basic_time, basic_price, unit_minute, unit_price = fees
    for x in records:
        time, car_number, command = x.split()
        hour, minute = time.split(":")
        time = int(hour) * 60 + int(minute)

        if car_number not in total:  # 누적 요금 위해서 차량번호마다 dict 정의
            total[car_number] = 0

        # 만약 IN 이면 park 에 {차량번호: 시간} 입력
        if command == "IN":
            if car_number not in park:
                park[car_number] = time

        # 만약 OUT 이면 park 에서 해당 넘버 데이터 제거 후 시간 계산
        if command == "OUT":
            in_time = park[car_number]
            use_time = time - in_time
            total[car_number] += use_time
            park.pop(car_number)  # 출차 처리

    # 출차 데이터 없는 녀석들 (park 남은 데이터) 처리 필요
    # 23시 59분 출차 처리
    for x in park:
        use_time = 1439 - park[x]
        total[x] += use_time

    for x in sorted(total):
        temp = basic_price
        total_time = total[x]
        if total_time <= basic_time:
            answer.append(temp)
        else:
            temp += math.ceil((total_time - basic_time) / unit_minute) * unit_price
            answer.append(temp)

    return answer


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

print(solution([120, 0, 60, 591],
               ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))

print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
