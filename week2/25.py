from collections import deque, defaultdict
import sys
input = sys.stdin.readline
K = int(input())


for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    q = deque()
    flag = False

    lDic = defaultdict(bool)
    rDic = defaultdict(bool)
   
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    

    for i in range(1, V + 1):
        if i in lDic:
            q.append((i, 1))
        elif i in rDic:
            q.append((i, -1))
        else:
            lDic[i] = True
            q.append((i, 1))

        while q:
            cur, pos = q.popleft()

            # 나랑 연결된 모든 노드에 대해 나랑 달라야 함.
            for nxt in graph[cur]:
                if (pos == 1 and nxt in lDic) or (pos == -1 and nxt in rDic): # 나랑 같으면 끝
                    print("NO")
                    flag = True
                    break
                
                # elif pos == 1 and : # 반대편에 있으면 무시.
                #     continue

                elif not nxt in lDic and not nxt in rDic: # 처음 온 노드면 넣기
                    if pos == 1:
                        rDic[nxt] = True
                    else:
                        lDic[nxt] = True
                    q.append((nxt, -pos))
        
            if flag:
                break
        if flag:
            break
    
    if not flag:
        print("YES")