# 데이터 개수 입력
n = int(input())
# 각 데이터를 공백 기준으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

# 단순히 공백 기분으로 구분하여 3개 입력만 받을 때
a, b, c = map(int, input().split())
print(a, b, c)

# 빠른 입력 받기 (입력값이 많을 때)
import sys
data = sys.stdin.readline().rstrip()
print(data)

a = 1
b = 2
print(a, b)
print(7, end=" ")
print(8, end=" ")

answer = 7
print("정답은 " + str(answer) + "입니다.")
print(f"정답은 {answer}입니다.")

