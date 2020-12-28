n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_count = [0] * (max(a) + 1)
b_count = [0] * (max(b) + 1)

for i in a:
    a_count[i] += 1

for i in b:
    b_count[i] += 1

a_list = []
b_list = []

for i in range(len(a_count)):
    for j in range(a_count[i]):
        a_list.append(i)


for i in range(len(b_count)):
    for j in range(b_count[i]):
        b_list.append(i)

for i in range(k):
    a_list[i], b_list[n - i - 1] = b_list[n - i - 1], a_list[i]

print(sum(a_list))