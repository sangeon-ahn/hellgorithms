import sys
input = sys.stdin.readline

import heapq

N = int(input())
nums = [int(input()) for _ in range(N)]

q = []

for n in nums:
    if n == 0:
        if not q:
            print(0)
        else:
            val = -heapq.heappop(q)
            print(val)
    else:
        heapq.heappush(q, -n)


