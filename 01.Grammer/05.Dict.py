data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("Word : 'Apple' exists")

print(data.keys())
print(data.values())

for key in data.keys():
    print(key)