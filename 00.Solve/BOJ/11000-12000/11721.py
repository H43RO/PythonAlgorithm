inArr = input()
cnt = 0
for each in inArr:
    print(each, end="")
    cnt = cnt + 1
    if (cnt % 10) == 0:
        print("")
