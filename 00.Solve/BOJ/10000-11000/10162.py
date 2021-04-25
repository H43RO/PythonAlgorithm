from sys import stdin, stdout

num = int(stdin.readline())

A, B, C = 300, 60, 10

count_A = num // A
num = num % A

count_B = num // B
num = num % B

count_C = num // C
num = num % C

if num != 0:
    print(-1)
else:
    print(count_A, count_B, count_C, end=' ')