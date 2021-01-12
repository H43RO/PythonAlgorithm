# 호출 회수를 담고 있는 DP Table
zero = [1, 0, 1]
one = [0, 1, 1]

# 호출 횟수마저 피보나치 규칙을 띄고 있음을 이용함

for case in range(int(input())):
    num = int(input())

    length = len(zero)
    if length <= num:
        for i in range(length, num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print(zero[num], one[num])
