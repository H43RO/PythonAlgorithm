n = int(input())

user = []

for i in range(n):
    data = dict()
    data['reg'] = i
    data['age'], data['name'] = input().split()
    data['age'] = int(data['age'])
    user.append(data)  # 가입 순서, 나이, 이름 입력

data = sorted(user, key=lambda x: (x['age'], x['reg']))

for x in data:
    print(str(x['age']) + " " + x['name'])
