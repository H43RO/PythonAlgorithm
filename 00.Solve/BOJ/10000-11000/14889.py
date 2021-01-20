from itertools import combinations, permutations
from collections import deque
from sys import stdin, stdout

n = int(stdin.readline())

people = list(range(n))
power = []
gap = []

case = deque(list(combinations(people, n // 2)))

for i in range(n):
    power.append(list(map(int, stdin.readline().split())))

while case:
    a = case.popleft()
    b = case.pop()

    a_member = list(permutations(a, 2))
    b_member = list(permutations(b, 2))

    a_power = 0
    b_power = 0

    for x in a_member:
        a_power += power[x[0]][x[1]]
    for x in b_member:
        b_power += power[x[0]][x[1]]

    gap.append(abs(a_power - b_power))

print(min(gap))