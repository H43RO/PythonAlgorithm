"""
   이분탐색을 활용한 풀이
"""
# from bisect import bisect_left
# from sys import stdin, stdout
#
# LIS = []
#
# n = int(stdin.readline().strip())
# num = list(map(int, input().split()))
#
# for i, v in enumerate(num):
#     if i == 0:
#         LIS.append(v)
#     else:
#         if LIS[len(LIS) - 1] < v:
#             LIS.append(v)
#         else:
#             LIS[bisect_left(LIS, v)] = v
#
# print(len(LIS))

"""
    DP 를 활용한 풀이
"""
from sys import stdin, stdout

n = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
dp = [0] * n

for i in range(n):
    for j in range(i):
        if data[i] > data[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
