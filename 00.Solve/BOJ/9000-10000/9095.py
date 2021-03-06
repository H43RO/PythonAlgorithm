# 사실 입력 범위가 11 보다 작기 때문에, 모든 해답을 알고 있는 상황이라서 충분히 O(1) 시간의 코드를 짤 수 있음
# 하지만 다이나믹 프로그래밍을 연습하고자 굳이 찾아낸 점화식을 활용하여 이렇게 짜보았음 (그래도 높은 수에 대한 범용성이 있음)

# 각 정수에 대한 해답 : [1, 2, 4, 7, 13, 24, 44, 81, 149, 274]

def solve(n):
    d = [0] * 11
    how = [0] * 11

    # 방법의 수 초기화
    d[1] = 1
    d[2] = 2
    d[3] = 4
    d[4] = 7

    # 감소량 초기화
    how[2] = 0
    how[3] = 0
    how[4] = 1

    if n in range(1, 5):
        return d[n]

    # i 번째 정수에 대한 방법의 수는 i - 1 번째 정수에 대한 방법의 수의 2배 한 값에다가
    # i - 1 번째 , i - 2 번째, i - 3 번째 감소량만큼 모두 빼준 값이 되는 규칙이 있음
    for i in range(5, n + 1):
        how[i] = how[i - 3] + how[i - 2] + how[i - 1]
        d[i] = d[i - 1] * 2 - how[i]

    return d[n]


case = int(input())

for i in range(case):
    print(solve(int(input())))
