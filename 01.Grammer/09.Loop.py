i = 1
result = 0

while i <= 9:
    result += i
    i += 1

print(result)

for i in range(0, 10):
    print(i, end=" ")
print()

array = [9, 8, 7, 6, 5]
array.sort()

for x in array:
    if x == array[len(array)-1]:
        print(x)
    else:
        print(x, end=" ")

result = 0
for i in range(1, 10):
    if i % 2 == 0:
        continue
    result += i

print(result)

score = [90, 85, 77, 65, 97]
for i in range(5):
    if score[i] >= 80:
        print(i + 1, "번 학생은 합격입니다")

print()

cheating_student_list = {2,4}
for i in range(5):
    if i + 1 in cheating_student_list:
        continue
    if score[i] >= 80:
        print(i + 1, "번 학생은 합격입니다")

for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i*j)
    print()