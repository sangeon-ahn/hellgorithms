from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = '0' + input().rstrip()
graph = [[] for _ in range(N + 1)]

ans = 0
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

    if A[u] == '1' and A[v] == '1':
        ans += 2

vis = [False] * (N + 1)

for i in range(1, N + 1):
    if A[i] == '0' and not vis[i]: # 실외면,
        cnts = 0

        # 해당 실외 영역 가장자리의 실내 개수를 구하기.
        q = deque()
        vis[i] = True
        q.append(i)

        while q:
            cur = q.popleft()

            for nxt in graph[cur]:
                if A[nxt] == '1': # 실내면 cnts에 추가
                    cnts += 1
                
                elif A[nxt] == '0' and not vis[nxt]: # 실외면 방문체크하고 큐에 추가
                    vis[nxt] = True
                    q.append(nxt)
            
        # while 끝났을 때, 해당 실외 영역 가장자리의 실내 개수 cnts 구함.
        if cnts > 0:
            ans += (cnts * (cnts - 1))

print(ans)

                    

        
        
        



