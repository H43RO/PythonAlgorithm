from sys import stdin

a, b = map(int, stdin.readline().split())
c = int(stdin.readline())
# 분 단위로 모두 환산
time = (a * 60) + b + c
# 만약 23시 59분을 초과하는 시간이라면
# 1440 (24:00) 를 빼줌
if time >= 1440:
    time -= 1440

# 시, 분 출력
print(time // 60, time % 60)
