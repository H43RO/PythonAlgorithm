from collections import deque
n, k = map(int, input().split())

people = deque()
result = []

for i in range(n):
    people.append(i + 1)

while people:
    for _ in range(k - 1):
        people.append(people.popleft())
    result.append(people.popleft())

result = ''.join(str(result))
result = result.replace("[", "<")
result = result.replace("]", ">")
print(result)

