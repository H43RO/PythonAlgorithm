def solution(board, moves):
    answer = 0
    stack = [[]]
    # 각 줄 정보를 기반으로 스택 리스트 생성
    for i in range(len(board[0])):
        temp = []
        for j in range(len(board) - 1, -1, -1):
            if board[j][i] != 0:
                temp.append(board[j][i])
        stack.append(temp)

    # 크레인 이동
    basket = []
    for x in moves:
        if not stack[x]:  # 해당 위치 스택이 비어잇다면
            continue  # 아무 동작도 하지 않음

        doll = stack[x].pop()  # 해당 위치 스택에서 인형 하나 뽑음
        if basket and basket[-1] == doll:  # 만약 바구니 최상단 인형과 동일하다면
            basket.pop()  # 바구니에서 꺼내고
            answer += 2  # 결과값 (터뜨린 인형 개수) 2 증가
        else:
            basket.append(doll)  # 일반적인 경우 바구니에 뽑은 인형 추가

    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
