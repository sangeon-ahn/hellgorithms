T = int(input())

for _ in range(T):
    ps = input()

    st = []
    flag = False
    for p in ps:
        if p == '(':
            st.append(p)
        
        else:
            if st:
                st.pop()
            else:
                print("NO")
                flag = True
                break
    
    if not flag:
        if st:
            print("NO")
        else:
            print("YES")
