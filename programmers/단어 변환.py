import sys

vis = []
ans = sys.maxsize
Words = []

def check(w1, w2):
    res = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            res += 1
    
    return res

def dfs(curW, target, cnts):
    global vis, ans
    
    for i in range(len(Words)):
        if vis[i]:
            continue
        
        diffCnts = check(curW, Words[i])

        if diffCnts > 1:
            continue

        elif diffCnts == 1:
            if Words[i] == target:
                ans = min(ans, cnts + 1)
                break

            else:
                vis[i] = True
                dfs(Words[i], target, cnts + 1)
                vis[i] = False
        
def solution(begin, target, words):
    global vis, ans, Words
    vis = [False] * len(words)
    Words = words
    
    dfs(begin, target, 0) # 현재 문자열, 타겟, 카운트 
    if ans == sys.maxsize:
        return 0
    return ans

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]

sol = solution(begin, target, words)

if ans == sys.maxsize:
    print(0)
else:
    print(sol)