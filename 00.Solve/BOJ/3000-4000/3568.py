from sys import stdin

text = stdin.readline().strip()[:-1]
text = text.split()
variable = ''.join(text[1:])
variable = variable.split(',')
common = text[0]

for x in variable:
    for i in range(len(x)):
        if x[i] == '[' or x[i] == '&' or x[i] == '*':
            var_name, var_type = x[:i], x[i:]
            break
    else:
        var_name, var_type = x, ''

    reform = ''
    for i in list(var_type)[::-1]:
        if i == ']':
            reform += '[]'
        elif i == '[':
            continue
        else:
            reform += i
    print(f'{common}{reform} {var_name};')
