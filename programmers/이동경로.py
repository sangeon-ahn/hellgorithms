answer = []
graph1 = []
graph2 = []

nameToIdx = {}
idxToName = {}
from collections import defaultdict
d = defaultdict(int)

def check(arr1, arr2):
    global idxToName
    for i in range(len(arr1)):
        if idxToName[arr1[i]] < idxToName[arr2[i]]:
            return False
    
    return True



def dfs(cur, cnts, target, airports):
    global answer
    if cnts == target:
        if len(answer) != target + 1:
            answer = airports
            return
        
        if check(answer, airports):
            answer = airports

        return
    
    for nxt in graph1[cur]:
        if graph2[cur][nxt] > 0:
            graph2[cur][nxt] -= 1
            dfs(nxt, cnts + 1, target, airports + [nxt])
            graph2[cur][nxt] += 1
            

        
def solution(tickets):
    global answer, graph1, graph2, idxToName, nameToIdx
    ticketCnts = len(tickets)
    graph1 = [[] for _ in range(10001)]
    graph2 = [[0] * (10001) for _ in range(10001)]
    idx = 1

    for tk in tickets:
        u, v = tk
        
        if u not in nameToIdx:
            nameToIdx[u] = idx
            idxToName[idx] = u
            idx += 1
        
        if v not in nameToIdx:
            nameToIdx[v] = idx
            idxToName[idx] = v
            idx += 1
        
        graph1[nameToIdx[u]].append(nameToIdx[v])
        graph2[nameToIdx[u]][nameToIdx[v]] += 1
    
    for i in range(idx):
        graph1[i].sort(key = lambda x: idxToName[x])
        
    
    dfs(nameToIdx["ICN"], 0, ticketCnts, [nameToIdx['ICN']])


    answer = map(lambda x: idxToName[x], answer)

    return list(answer)

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

sol = solution(tickets)
print(sol)

    