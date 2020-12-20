x = 15

if x >= 10:
    print("x >= 10")

if x >= 0:
    print("x >= 0")

if x >= 30:
    print("x >= 30")
elif x >= 20:
    print("x >= 20")
else:
    print("x <= 20, x <= 30")

if True or False:
    print("YES")

if True and False:
    print("YES")

a = 15

if a <= 20 and a >= 0:
    print("YES")

if 0 <= a <= 20:
    print("YES!")

score = 85
if score >= 80:
    pass  # NOP (디버깅에 사용)
else:
    print('성적이 80점 미만입니다')

result = "Success" if score >= 80 else "Fail"
print(result)
