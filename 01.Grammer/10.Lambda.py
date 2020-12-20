def add(a, b):
    return a + b


print(add(3, 4))


def add(a, b):
    print(a + b)


add(3, 4)


def substract(a, b):
    print(a - b)


substract(b=3, a=2)

a = 0


def func():
    global a  # 함수 스코프 바깥의 a 변수 사용
    a += 1
    print(a)


func()

array = [1, 2, 3, 4, 5]


def func():
    array.append(6)
    print(array)


func()


def operator(a, b):
    add_var = a + b
    sub_var = a - b
    mul_var = a * b
    div_var = a / b
    return add_var, sub_var, mul_var, div_var


a, b, c, d = operator(8, 4)
print(a, b, c, d)
