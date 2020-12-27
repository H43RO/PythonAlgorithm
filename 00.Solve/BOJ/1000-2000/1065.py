num = int(input())

result = 0

# 3자리 숫자에 대해서 입력됨 (어차피 1000은 한수가 아님)
for i in range(1, num + 1):
    if i <= 99:
        result += 1

    else:
        nums = list(map(int, str(i)))
        if nums[0] - nums[1] == nums[1] - nums[2] :
            result += 1

print(result)
