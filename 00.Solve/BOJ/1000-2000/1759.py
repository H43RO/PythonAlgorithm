from itertools import combinations

L, C = map(int, input().split())
word = set(input().split())

moeum = set(['a', 'e', 'i', 'o', 'u'])
word_moeum = word & moeum

for x in combinations(sorted(word), L):
    moeum_count = len(set(x) & word_moeum)
    if moeum_count == 0 or L - moeum_count < 2:
        continue
    print(''.join(x))
