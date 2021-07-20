from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(1000000)


# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수, 간선의 개수 입력 받기
v, e = map(int, stdin.readline().split())
parent = [i for i in range(v + 1)]  # 부모 초기화

# Union 연산을 각각 수행
for i in range(e):
    op, a, b = map(int, stdin.readline().split())
    if op == 1:
        stdout.write('YES\n' if find_parent(parent, a) == find_parent(parent, b) else 'NO\n')
    else:
        union_parent(parent, a, b)
