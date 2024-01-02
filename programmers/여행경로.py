from collections import defaultdict

def dfs(graph, N, key, footprint):
    print(footprint)

    if len(footprint) == N + 1:
        return footprint
    
    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)

        tmp = footprint[:]
        tmp.append(country)

        ret = dfs(graph, N, country, tmp)

        graph[key].insert(idx, country)

        if ret:
            return ret

def solution(tickets):
    answer = []

    graph = defaultdict(list)

    N = len(tickets)
    for tk in tickets:
        graph[tk[0]].append(tk[1])
        graph[tk[0]].sort()
    
    answer = dfs(graph, N, "ICN", ["ICN"])
    return answer