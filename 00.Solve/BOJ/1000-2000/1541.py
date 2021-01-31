from sys import stdin, stdout

# 입력 표현식
exp = stdin.readline().strip()
exp = exp.lstrip("0")

# 예외를 처리한 최종 표현식이 담길 변수
exp_result = []

# 숫자를 한 뭉태기로 저장하기 위한 임시 변수
temp = ''

# '-' 연산자가 등장하면 플래그 발동
minus = False

# 각 숫자와 연산자를 분리하여 리스트에 저장
for i, v in enumerate(exp):
    # '-' 연산자는 그대로 리스트에 저장 (최솟값 유도)
    if v == '-':
        minus = True
        exp_result.append('-')
    elif v == '+':
        # '-' 연산자를 만난 적 있으면 '+' 대신 '-' 삽입
        if minus:
            exp_result.append('-')
        # '-' 연산자를 만난 적 없으면 '+' 삽입
        else:
            exp_result.append('+')
    else:
        # 한 숫자가 완성되면 맨 앞의 0을 모두 제거하고 저장 (예외 처리)
        if i == len(exp) - 1 or exp[i + 1] == '-' or exp[i + 1] == '+':
            temp += v
            temp = temp.lstrip("0")
            exp_result.append(temp)
            temp = ''
        # 숫자가 완성된게 아니라면 임시 변수에 숫자 추가
        else:
            temp += v

print(eval(''.join(exp_result)))
