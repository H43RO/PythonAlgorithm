piece = list(map(int, input().split()))

num = [1, 1, 2, 2, 2, 8]

for i, v in enumerate(piece):
    print(num[i] - v, end=' ')
