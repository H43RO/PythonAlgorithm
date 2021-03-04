from sys import stdin, stdout

n = int(stdin.readline())
weight = list(map(int, stdin.readline().split()))

# 측정할 수 없는 수를 1 부터 탐색해봄
result = 1

# 무게 추 각각에 대하여 탐색해보았을 때
for x in sorted(weight):
    # 현재 탐색 중인 무게추 보다 result 가 더 크면
    if result >= x:
        # 무제추 무게만큼 result 더해줌
        result += x

# 추의 무게들을 합친 무게까지가 그 추들을 이용하여 측정할 수 있는 무게의 한계
# 결국, 무게추들의 무게 합 + 1 = 추들이 측정할 수 없는 최소 무게
print(result)
