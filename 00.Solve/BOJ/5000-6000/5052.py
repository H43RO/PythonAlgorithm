from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())
    numbers = sorted([stdin.readline().strip() for _ in range(n)])
    available = True
    for i in range(n - 1):
        if numbers[i] in numbers[i + 1][:len(numbers[i])]:  #
            available = False
            break
    if available:
        print("YES")
    else:
        print("NO")

'''
1
2
1
21
이 경우에
1이 21 내에 포함되어 있어서
자꾸 틀린 답을 출력해서 삽질했다.
비교할 길이만큼 문자열을 잘라서 비교하여 해결했다.
'''