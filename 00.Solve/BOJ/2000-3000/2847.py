from sys import stdin

n = int(stdin.readline())
data = [int(stdin.readline()) for _ in range(n)]

result = 0
for i in range(n - 2, -1, -1):  # 뒤에서 부터 점수 감소
    if data[i + 1] <= data[i]:  # 뒷 레벨보다 레벨이 높다면
        temp = data[i] - data[i + 1] + 1
        data[i] -= temp  # 뒷 레벨보다 1만큼 작도록 레벨을 낮춤
        result += temp   # 레벨 감소 횟수 증가
print(result)
