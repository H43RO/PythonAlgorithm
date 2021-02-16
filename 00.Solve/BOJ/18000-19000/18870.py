from sys import stdin, stdout

n = int(stdin.readline().strip())
data = list(map(int, stdin.readline().split()))
sorted_data = sorted(set(data))
sorted_data = {sorted_data[i]: i for i in range(len(sorted_data))}

print(*[sorted_data[i] for i in data])
