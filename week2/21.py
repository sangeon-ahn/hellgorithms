from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(N):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(len(graph)):
    graph[i].sort()

vis = [False] * (N + 1)

def dfs(node):
    vis[nxt] = True
    print(node, end = ' ')

    for nxt in graph[node]:
        if vis[nxt]:
            continue

        dfs(nxt)

def bfs(node):
    q = deque()
    vis[node] = True
    q.append(node)

    while q:
        cur = q.popleft()
        print(cur, end = ' ')

        for nxt in graph[cur]:
            if vis[nxt]:
                continue

            vis[nxt] = True
            q.append(nxt)

dfs(V)
print()

for i in range(N + 1):
    vis[i] = False

vis[V] = True
bfs(V)

    
    
