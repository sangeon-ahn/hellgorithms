T = int(input())
for _ in range(T):
    ip = input().split()

    R = int(ip[0])
    S = ip[1]

    res = ""
    for i in range(len(S)):
        res += S[i] * R
    
    print(res)

