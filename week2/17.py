import sys, heapq
input = sys.stdin.readline

N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
D = int(input())

for line in lines:
    if line[0] > line[1]:
        temp = line[0]
        line[0] = line[1]
        line[1] = temp

lines.sort(key = lambda line: (line[1], line[0]))

q = []
ans = 0
for line in lines:
    # 어떤 기준으로 정렬? -> 맨왼쪽 지점 기준 오름차순
    heapq.heappush(q, line[0])

    # 우큐에 있는 것들중 D를 벗어나는 것들을 모두 pop
    while q and q[0] < line[1] - D:
        heapq.heappop(q)
    
    ans = max(ans, len(q))

print(ans)


