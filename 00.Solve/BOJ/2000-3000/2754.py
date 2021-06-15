from sys import stdin

major = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0}
minor = {'+': 0.3, '0': 0.0, '-': -0.3}

grade = stdin.readline().strip()
result = 0.0

if len(grade) > 1:
    result += major[grade[0]]
    result += minor[grade[1]]

print(result)
