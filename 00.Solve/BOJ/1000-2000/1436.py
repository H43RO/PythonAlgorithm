a = int(input())
data = []

for i in range(666, 10000000):
    if len(data) > 10000:  # 어차피 찾고자 하는 수는 10000번째 이하
        break

    j = str(i)
    # 666 이 포함되어 있으면 목록에 추가
    if j.find("666") != -1:
        data.append(j)

print(data[a-1])