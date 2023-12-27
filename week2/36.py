from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
coins = list(set(int(input().rstrip()) for _ in range(N)))
coins.sort()

ans = sys.maxsize

checked = [False] * 10001 # K <= 10,000

q = deque() # i, cnts, val

for i in range(len(coins)):
    if coins[i] <= 10000:
        q.append((i, 1, coins[i]))
        checked[coins[i]] = True

if min(coins) > K:
    print(-1)
    sys.exit()
    
def bfs():
    global ans
    while q:
        curPos, cnts, curSum = q.popleft()
        if curSum == K:
            ans = min(ans, cnts)
            return

        for i in range(curPos, len(coins)):
            nextSum = curSum + coins[i]
            if nextSum > K:
                break 

            elif nextSum == K:
                ans = min(ans, cnts + 1)
                return
            
            else:
                if not checked[nextSum]:
                    checked[nextSum] = True
                    q.append((curPos, cnts + 1, nextSum))

bfs()
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)


