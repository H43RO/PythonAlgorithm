from sys import stdin

n, k = map(int, stdin.readline().split())
quest_list = sorted(list(map(int, stdin.readline().split())))

exp = 0  # 스톤에 모을 수 있는 경험치 합
stone = 0  # 활성화 스톤 개수

for quest in quest_list:
    exp += (quest * stone)
    stone = min(k, stone + 1)  # 활성화 스톤 개수가 K 를 안 넘도록

print(exp)
