import sys
input = sys.stdin.readline

ps = input()
st = []

# 1. 올바른 괄호열인지부터 체크
def check(ps):
    for ch in ps:
        if ch == '(' or ch == '[':
            st.append(ch)
        
        elif ch == ')':
            if not st or st[-1] != '(':
                return False
            else:
                st.pop()
        
        elif ch == ']':
            if not st or st[-1] != '[':
                return False
            else:
                st.pop()
    
    if st:
        return False
    return True

if not check(ps):
    print(0)
    sys.exit()

mul = 1
ans = 0
for i in range(len(ps)):
    if ps[i] == '(':
        mul *= 2
        st.append(ps[i])
    
    elif ps[i] == '[':
        mul *= 3
        st.append(ps[i])
    
    elif ps[i] == ')':
        if ps[i - 1] != ']' and ps[i - 1] != ')':
            ans += mul
        mul //= 2 
    
    elif ps[i] == ']':
        if ps[i - 1] != ']' and ps[i - 1] != ')':
            ans += mul
        mul //= 3

print(ans)
        
        

    

