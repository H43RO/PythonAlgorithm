from sys import stdin

roma = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
arabic = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

A = list(stdin.readline().strip())
B = list(stdin.readline().strip())

sum_total = roma[A[-1]]
for i, v in enumerate(A):
    if i < len(A) - 1:
        if roma[v] < roma[A[i + 1]]:
            sum_total -= roma[v]  # 뒤에 더 큰 숫자가 있다면 값 빼줌
        else:
            sum_total += roma[v]

sum_total += roma[B[-1]]
for i, v in enumerate(B):  # 위 루프와 동일 로직
    if i < len(B) - 1:
        if roma[v] < roma[B[i + 1]]:
            sum_total -= roma[v]
        else:
            sum_total += roma[v]

print(sum_total)

roma_result = []
for x in reversed(arabic.keys()):  # 큰 숫자부터 차례로 처리
    while x <= sum_total:
        # 처리해줘야 할 예외 숫자는 4 아니면 9로 시작
        if str(sum_total).startswith('4'):
            sum_total -= 4 * x
            roma_result.append(arabic[x])
            roma_result.append(arabic[x * 5])
        elif str(sum_total).startswith('9'):
            x //= 5
            sum_total -= 9 * x
            roma_result.append(arabic[x])
            roma_result.append(arabic[x * 10])
        else:
            sum_total -= x
            roma_result.append(arabic[x])

print(''.join(roma_result))