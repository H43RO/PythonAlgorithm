# 탐욕법으로 얻은 해가 결국 최적의 해가 된다는 사실을 추론할 수 있어야 풀 수 있는 문제들이 출시되는 편

n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
array = [500, 100, 50, 10]

for coin in array:
    count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전 개수 세기
    n %= coin

print(count)
