num = list(map(int, input().split()))

set_num = set(num)

# 중복되는 숫자가 없을 때
if len(set_num) == 3:
    print(max(num) * 100)
elif len(set_num) == 2:
    for x in num:
        if num.count(x) == 2:
            print(1000 + (x * 100))
            break
else:
    print(10000 + (set_num.pop() * 1000))