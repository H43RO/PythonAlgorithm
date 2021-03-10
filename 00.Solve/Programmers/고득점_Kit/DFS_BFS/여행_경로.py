# 알파벳 순으로 순회하되, 모든 도시를 방문할 수 없는 경우 정답이 아님
def dfs(graph):
    stack = ["ICN"]
    path = []

    while stack:
        top = stack[-1]
        # 특정 공항에서 출발하는 표가 없거나
        # 더 이상 쓸 수 있는 티켓이 없는 경우
        if top not in graph or len(graph[top]) == 0:
            path.append(stack.pop())
        # 그런게 아니라면 알파벳 순으로 정렬한 것들 중 맨 앞 티켓 사용
        else:
            stack.append(graph[top].pop(0))
    return path[::-1]


def solution(tickets):
    graph = dict()
    graph["ICN"] = []
    for x in tickets:
        if x[0] in graph:
            graph[x[0]].append(x[1])
        else:
            graph[x[0]] = []
            graph[x[0]].append(x[1])

        graph[x[0]].sort()

    return dfs(graph)


print(solution([['ICN', 'B'], ['B', 'C'], ['C', 'ICN'], ['ICN', 'D'], ['ICN', 'E'], ['E', 'F']]))

# [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

# ['ICN', 'B'], ['B', 'C'], ['C', 'ICN'], ['ICN', 'D'], ['ICN', 'E'], ['E', 'F']
# ['ICN', 'B', 'C', 'ICN', 'E', 'F', 'D']

# ['ICN' ,'B'], ['ICN', 'C'] ,['C', 'D'], ['D', 'ICN']
# ['ICN', 'C', 'D', 'ICN', 'B']
