from sys import stdin, maxsize


# 모든 연산 경우의 수에 대해 재귀 탐색
def solve(i, result, add, sub, mul, div):
    global max_result, min_result
    if i >= n:  # 주어진 수의 개수만큼 연산을 했다면 결과값 갱신
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    if add > 0:  # + 개수 남아있으면 더하기 연산 수행 (개수 1개 차감)
        solve(i + 1, result + num[i], add - 1, sub, mul, div)
    if sub > 0:  # - 개수 남아있으면 빼기 연산 수행 (개수 1개 차감)
        solve(i + 1, result - num[i], add, sub - 1, mul, div)
    if mul > 0:  # * 개수 남아있으면 곱하기 연산 수행 (개수 1개 차감)
        solve(i + 1, result * num[i], add, sub, mul - 1, div)
    if div > 0:  # / 개수 남아있으면 나누기 연산 수행 (개수 1개 차감)
        solve(i + 1, int(result / num[i]), add, sub, mul, div - 1)


n = int(stdin.readline())
num = list(map(int, stdin.readline().split()))
add, sub, mul, div = map(int, stdin.readline().split())

# 최댓값, 최솟값을 갱신하도록 함
max_result = -maxsize - 1  # 계산할 수 있는 수 중 가장 작은 값
min_result = maxsize  # 계산할 수 있는 수 중 가장 큰 값

solve(1, num[0], add, sub, mul, div)

print(max_result)
print(min_result)
