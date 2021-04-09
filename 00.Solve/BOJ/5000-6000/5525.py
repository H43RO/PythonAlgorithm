from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
s = stdin.readline().strip()

IOI = 0
count = 0

'''
 처음에 startswith() 를 응용한 O(n^2) 코드로 풀었다가 시간초과 발생
 전체 문자열에 대하여 딱 한 번의 탐색 O(n) 으로 동작이 끝나야 통과하는 듯
'''

i = 0
while i < m - 2:
    if s[i:i + 3] == "IOI":  # 현재 인덱스로부터 IOI 가 발견되면
        IOI += 1  # IOI 등장횟수 1 증가

        if IOI == n:    # 만약 N만큼 등장했다면 (탐색하고자 하는 패턴과 일치)
            count += 1  # - P(n) 패턴 발견횟수 (결과) 1 증가
            IOI -= 1    # - 연달아 등장할 패턴에 대비해 등장 횟수 1 줄임
        i += 2  # 'IO' 만큼 인덱스 건너뜀

    else:  # 만약 패턴이 발견되지 않으면
        IOI = 0  # - 패턴 등장횟수 초기화 및 인덱스 1 증가
        i += 1

print(count)
