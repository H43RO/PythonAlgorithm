from sys import stdin, stdout
from collections import deque

n = int(stdin.readline())
meeting = []

for i in range(n):
    meeting.append(list(map(int, stdin.readline().split())))

# 끝나는 시간이 빠른 순으로 정렬 (끝나는 시간이 같으면 시작하는 시간이 빠른 순으로 정렬)
# 맨 첫 회의를 고르는 상황에 왜냐하면 끝나는 시간이 같은데 (3, 3) (1, 3) 와 같이 입력됐다면
# 정렬 결과 상 (1, 3) 을 고르지 않고 (3, 3) 을 골라버리기 때문에 손해가 발생하기 때문
meeting.sort(key=lambda x: (x[1], x[0]))

meeting = deque(meeting)
result = 1
end_time = meeting.popleft()[1]

while meeting:
    # 끝 시간과 시작 시간이 같은 경우도 회의가 가능한건지 모르고
    # meeting[0][0] > end_time 이라고 했다가 오답 처리 됨
    if meeting[0][0] >= end_time:  # 회의 시작 시간이 이전 회의 종료 시간 이후라면
        result += 1
        end_time = meeting.popleft()[1]
    else:
        meeting.popleft()

print(result)