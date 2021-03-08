def promising(i, col):
    k = 1
    flag = True
    while k < i and flag:
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            flag = False
        k += 1
    return flag


def n_queens(i, col):
    n = len(col) - 1
    if promising(i, col):
        if i == n:
            print(col[1: n + 1])
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                n_queens(i + 1, col)


"""
    백 트래킹 = DFS + 가지치기(Pruning) 
    - 상태 공간 트리 (해답 탐색을 위해 트리 형태의 구조로 임의적, 암묵적으로 해석한 자료구조) 활용
    - 상태 공간 트리는 해를 찾기 위해 탐색해야 하는 모든 경로를 포함함
    
    1. 트리를 DFS 로 탐색하는 과정에서, 현재 경로가 조건을 만족하는 해가 될 수 있는지 판단
    2. 이 때, 해가 될 가능성이 있는 것을 Promising 하다고 함.
    3. 현재 경로가 만약 Non-Promising 하다면, 탐색을 중지하고 부모 노드로 되돌아감 (Pruning, 가지치기)
    
    # 재귀로 구현하는 일반적인 백트래킹 알고리즘 형태
    
    void checkNode(node v){
        node u;
        if (promising(v)){
            if (v 에 해답이 존재하면){
                return 해답;
            }
        } else{
            for (v 의 모든 자식 노드 u 에 대하여){
                checkNode(u);
            }
        }
    }

    N-Queens 경우의 수를 고려하고자 백 트래킹을 활용할 때,
    col 이라는 리스트는 각 Column 의 Queen 의 위치를 의미함.
    
    예를들어 4 X 4 체스판에서의 N-Queens 문제일 때
    col 리스트가 [2, 4, 3, 1] 이라고 되어있다면
    첫 번째 행의 2번째 열에 하나,
    두 번째 행의 4번째 열에 하나,
    세 번째 행의 3번째 열에 하나,
    네 번째 행의 1번째 열에 하나씩 퀸이 배치되어 있는 것이다.
"""

n = int(input())
col = [0] * (n + 1)
n_queens(0, col)
