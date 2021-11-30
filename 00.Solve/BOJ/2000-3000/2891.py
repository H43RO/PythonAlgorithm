from sys import stdin

n, S, R = map(int, stdin.readline().split())
damaged = list(map(int, stdin.readline().split()))
left = list(map(int, stdin.readline().split()))

# 여분 갖고 있는 팀 탐색
for x in left:
    if x in damaged:  # 1순위 : 여분 갖고 왔는데 부셔졌는 지
        del damaged[damaged.index(x)]
        continue
    if x - 1 in damaged:  # 2순위 : 자기 앞 번호 팀 부셔졌는 지
        del damaged[damaged.index(x - 1)]
        continue
    if x + 1 in damaged:  # 3순위 : 자기 뒷 번호 팀 부셔졌는 지
        del damaged[damaged.index(x + 1)]

print(len(damaged))
