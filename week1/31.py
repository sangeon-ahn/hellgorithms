N, r, c = map(int, input().split())


def recur(length, r, c):
    if length == 1:
        return 1
    
    area = (length // 2)**2
    newR = r
    newC = c

    if r < length // 2:
        # 2사분면
        if c < length // 2:
            area *= 0
        # 1사분면
        else:
            area *= 1
            newC -= length // 2
    else:
        # 3사분면
        if c < length // 2:
            area *= 2
            newR -= length // 2
        # 4사분면
        else:
            area *= 3
            newR -= length // 2
            newC -= length // 2
    
    rest = recur(length // 2, newR, newC)
    
    return area + rest

ans = recur(2**N, r, c) - 1
print(ans)