from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    a, b = stdin.readline().strip().split()

    if len(a) != len(b):
        print(f"{a} & {b} are NOT anagrams.")
        continue

    # 두 문자열을 오름차순으로 정렬해봤을 때 원소가 모두 같다면 애너그램
    if sorted(a) == sorted(b):
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")
