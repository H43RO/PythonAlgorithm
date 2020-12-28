m = int(input())

weight = [0] * m
height = [0] * m
rank = [0] * m

for i in range(m):
    weight[i], height[i] = map(int, input().split())

for i in range(m):
    superior = 0
    for index, value in enumerate(weight):
        if weight[i] < value:
            if height[i] < height[index]:
                superior += 1
    rank[i] = superior + 1

for x in rank:
    print(x, end=' ')