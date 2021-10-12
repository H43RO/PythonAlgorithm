from sys import stdin


def sort_graph(graph, command):
    result = []

    if command == "C":  # 연산의 편의를 위해 전치시킴
        graph = list(map(list, zip(*graph)))

    # R, C 공통 연산
    for x in graph:  # 행 한 줄씩 탐색
        temp = []
        count = []
        for a in set(x):  # 해당 행에 등장하는 숫자들 하나씩 순회
            if a == 0:  # 만약 0이면 제낌
                continue
            count.append((a, x.count(a)))  # 해당 숫자와 행에 몇 번 등장했는지와 함께 저장

        for num, cnt in sorted(count, key=lambda x: (x[1], x[0])):  # 등장 횟수 오름차순, 숫자 오름차순으로 정렬된 리스트 순회
            temp.extend([num, cnt])  # temp 리스트에 숫자와 등장횟수 넣어줌

        result.append(temp)  # 한 행에 대한 정렬 결과를 result 에 넣어줌

    # 위 연산이 끝나게 되면, result 에 모든 행들이 정렬되어 저장돼있음
    for x in result:  # 행 한 줄씩 탐색
        while len(x) < len(max(result, key=lambda x: len(x))):  # 현재 행이 가장 긴 행보다 짧다면
            x.append(0)  # 길이가 같아질 때까지 0 추가
        x = x[:100]  # 만약 길이가 100이 넘어가면 100 넘어가는 부분 몽땅 버림

    if command == "C":  # 만약 C 연산이었다면, 마지막에 다시 전치시켜야 함 (원상 복구)
        result = list(map(list, zip(*result)))

    return result


r, c, k = map(int, stdin.readline().split())
data = [list(map(int, stdin.readline().split())) for _ in range(3)]

for i in range(101):  # 100초 세기
    # 만약 data[r - 1][c - 1] 가 범위를 넘지 않고, k 값이 들어있다면 시간 출력 후 종료
    if 0 <= r - 1 < len(data) and 0 <= c - 1 < len(data[0]) and data[r - 1][c - 1] == k:
        print(i)
        exit(0)

    # 행의 개수 >= 열의 개수인 경우 R 연산, 행의 개수 < 열의 개수인 경우 C 연산
    command = "R" if len(data) >= len(data[0]) else "C"
    data = sort_graph(data, command)

print(-1)  # 100초 지나도 안 되면 -1 출력
