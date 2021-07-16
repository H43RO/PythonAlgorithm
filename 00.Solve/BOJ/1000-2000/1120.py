from sys import stdin

a, b = stdin.readline().split()
diff = len(b) - len(a) + 1
result = len(b)  # 최악의 경우

# 어차피 a 문자열 양쪽에 그 어떤 알파벳도 붙여볼 수 있기 때문에
# b 내에서 a 슬라이드 윈도우를 옮기면서 가장 차이가 없는 부분을 찾으면 됨
for i in range(diff):
    temp = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            temp += 1
    result = min(result, temp)

print(result)
