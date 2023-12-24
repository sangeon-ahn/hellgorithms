T = int(input())

def eratos(size):
    result = [True for _ in range(size + 1)]
    result[0] = False
    result[1] = False

    for i in range(2, size + 1): # size + 1까지 안해도 되고 size // 2까지만 해도 됨.
        if not result[i]:
            continue

        for j in range(i * i, size + 1, i):
            result[j] = False
    
    return result

isSosu = eratos(10000)

for _ in range(T):
    num = int(input())

    l = num // 2
    r = num // 2

    for i in range(l):
        if isSosu[l] and isSosu[r]:
            print(f"{l} {r}")
            break
        else:
            l -= 1
            r += 1
    

