num = input()

while num != '0':
    if num[::-1] == num:
        print('yes')
    else:
        print('no')
    num = input()