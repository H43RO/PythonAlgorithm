from sys import stdin
'''
    T -> S 로 역순으로 접근
    - 문자열 뒤에 A 를 추가한다 -> 문자열 뒤의 A 를 제거한다
    - 문자열을 뒤집고 뒤에 B 를 추가한다 -> 문자열 뒤의 B 를 제거하고 뒤집는다
    
    -> 만약 길이가 같을 때 두 문자열이 같다면 1 출력, 아니면 0 출력 
'''
s = list(stdin.readline().strip())
t = list(stdin.readline().strip())

while len(t) >= len(s):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if s == t:
        print(1)
        exit()
print(0)
