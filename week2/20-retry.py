V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key = lambda edge: edge[2]) # 가중치 기준 오름차순.

group = [i for i in range(V + 1)]

def union(node1, node2): # node1이 node2를 흡수.
    group[node2] = node1
    
def find(node):
    nodeGroup = group[node]

    if node != nodeGroup:
        nodeGroup = find(nodeGroup)
    
    group[node] = nodeGroup
    return nodeGroup
    

ans = 0
for edge in edges:
    u, v, w = edge

    uGroup = find(u)
    vGroup = find(v)

    if uGroup != vGroup:
        union(uGroup, vGroup)
        ans += w

print(ans)    
    

    
