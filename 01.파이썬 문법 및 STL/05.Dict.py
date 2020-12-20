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

b = {
    '홍길동': 96,
    '이순신': 98
}

print(b)
print(b['홍길동'])
print(b.keys())
key_list = list(b.keys())  # List Type 으로 캐스팅
print(key_list)