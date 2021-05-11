from sys import stdin

n, p = map(int, stdin.readline().split())

guitar = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
result = 0

for _ in range(n):
    string, fret = map(int, stdin.readline().split())

    # 더 높은 프렛에 있는 모든 손가락을 떼어야 함
    while guitar[string] and guitar[string][-1] > fret:
        guitar[string].pop()
        result += 1

    # 만약 줄이 비어있거나 타겟보다 더 높은 프렛에 손가락이 없다면 타겟 프렛에 손가락 올림
    # 따라서, 이미 타겟 프렛에 손가락이 올라가있었다면 패스
    if not guitar[string] or guitar[string][-1] < fret:
        guitar[string].append(fret)
        result += 1

print(result)
