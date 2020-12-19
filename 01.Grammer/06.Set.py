data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

data = {1, 1, 2, 3, 4, 4, 5}
print(data)
print()

a = {1,2,3}
print(a)

a.add(4)
print(a)

a.update([5,6])
print(a)

a.remove(3)
print(a)
print()

a = {1,2,3,4,5}
b = {3,4,5,6,7}

print(a | b)  # 합집합
print(a & b)  # 교집합
print(a - b)  # 차집합