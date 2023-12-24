import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
tops = list(map(int, input().split()))
st = [] # 높은 탑들만 남아있는 스택
ans = []

for i in range(len(tops)):
    if not st: # 스택 비어있으면 내 앞에 아무것도 없다는뜻
        ans.append(0)
    else:
        while st and tops[st[-1]] < tops[i]: # 내가 스택 탑보다 크면 pop
            st.pop()
        
        # 다 pop돼서 st에 남은게 없으면 0 
        if not st:
            ans.append(0)
        
        # 남아 있으면 st top이 답.
        else:
            ans.append(st[-1] + 1)

    st.append(i)

for n in ans:
    print(n, end = ' ')
            

    

    


    