from sys import stdin


# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(stdin.readline())
m = int(stdin.readline())

parent = [0] * (n + 1)  # 부모 테이블 초기화
# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(1, n + 1):
    temp = list(map(int, stdin.readline().split()))
    for j in range(n):
        if temp[j] == 0:
            continue
        union_parent(parent, i, j + 1)

trip = list(map(int, stdin.readline().split()))
result = []
for x in trip:
    temp = find_parent(parent, x)
    if not result:
        result.append(temp)
        continue
    if temp not in result:
        print("NO")
        exit(0)
print("YES")


