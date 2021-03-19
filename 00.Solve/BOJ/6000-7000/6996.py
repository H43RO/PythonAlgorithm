from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    a, b = stdin.readline().strip().split()

    if sorted(a) == sorted(b):
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")
