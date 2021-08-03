from sys import stdin

n = int(stdin.readline())
weight = sorted(list(map(int, stdin.readline().split())))

result = 1  # 추의 누적합 저장

for x in weight:          # 무게 순으로 정렬한 추 리스트에 대하여
    if result >= x:       # 누적합 보다 작거나 같은 무게의 추를 만났을 때
        result += x       # 이 추의 무게를 누적합에 더해줌

print(result)
