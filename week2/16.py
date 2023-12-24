import heapq, sys
input = sys.stdin.readline

q = []
N = int(input())
nums = [int(input()) for _ in range(N)]

for n in nums:
    heapq.heappush(q, n)

ans = 0
while len(q) >= 2:
    n1 = heapq.heappop(q)
    n2 = heapq.heappop(q)
    ans += n1 + n2
    heapq.heappush(q, n1 + n2)

print(ans)
    



