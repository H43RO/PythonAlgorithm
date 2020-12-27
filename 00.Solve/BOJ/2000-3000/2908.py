a, b = input().split()
a_list = list(a)
b_list = list(b)

a_list.reverse()
b_list.reverse()

a_num = int(''.join(a_list))
b_num = int(''.join(b_list))

print(max(a_num, b_num))
