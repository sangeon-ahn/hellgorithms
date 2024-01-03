import heapq
def solution(n, edge):
    answer = 0

    hq = []
    graph = [[] for _ in range(n + 1)]
    for e in edge:
        u, v = e
        graph[u].append(v)
        graph[v].append(u)
    
    dist = [float('inf')] * (n + 1) # 1 -> node 거리
    dist[1] = 0
    
    heapq.heappush(hq, (0,1)) # (누적 거리, 현재 위치)
    
    while hq:
        [curDist, curPos] = heapq.heappop(hq)

        if dist[curPos] != curDist:
            continue

        for nxt in graph[curPos]:
            if dist[nxt] > curDist + 1:
                dist[nxt] = curDist + 1
                heapq.heappush(hq, (dist[nxt], nxt))
    
    print(dist)
    maxDist = max(dist[1:])

    for val in dist:
        if maxDist == val:
            answer += 1
    
    return answer
    


n = 6	
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
sol = solution(n, vertex)
print(sol)