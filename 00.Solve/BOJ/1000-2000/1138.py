from sys import stdin

n = int(stdin.readline())
# 키 큰 사람부터 내림차순으로 처리하기 위해 입력받은 정보를 뒤집음
people = list(reversed(list(map(int, stdin.readline().split()))))

data = []
for i, v in enumerate(people):
    data.insert(v, n - i)  # '왼쪽에 몇 명 있는 지' 라는 값 자체가 인덱스가 됨

print(' '.join(str(x) for x in data))
