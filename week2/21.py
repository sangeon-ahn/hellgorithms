from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(N):
    u, v = map(int, input().split())
    
    if graph[u]
    graph[u].append(v)
    graph[v].append(u)

for arr in graph:
    arr.sort()

vis = [False] * (N + 1)

def dfs(node):
    print(node, end = ' ')

    for nxt in graph[node]:
        if vis[nxt]:
            continue

        vis[nxt] = True
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

vis[V] = True
dfs(V)
print()

vis = [False] * (N + 1)
bfs(V)

    
    
