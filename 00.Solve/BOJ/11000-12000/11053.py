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
#         if LIS[-1] < v:
#             LIS.append(v)
#         else:
#             LIS[bisect_left(LIS, v)] = v
#
# print(len(LIS))
#

"""
    DP 를 활용한 풀이
"""

from sys import stdin

n = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
dp = [0] * n

for i in range(n):
    # 이전 데이터들을 탐색해봤을 때
    for j in range(i):
        # 숫자가 더 작은데 DP 값은 더 큰 놈을 발견하면 DP 갱신
        if data[i] > data[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    # 가장 DP 큰 놈에 + 1 해서 저장
    dp[i] += 1
print(max(dp))
