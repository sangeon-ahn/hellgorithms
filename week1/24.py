W, H = map(int, input().split())
L = int(input())
garos = [0]
seros = [0]

for _ in range(L):
    t, pos = map(int, input().split())

    if t == 0: # 가로면,
        garos.append(pos)
    else:
        seros.append(pos)

garos.append(H)
seros.append(W)

garos.sort()
seros.sort()

maxArea = 0
for i in range(len(garos) - 1):
    widthDiff = garos[i + 1] - garos[i]

    for j in range(len(seros) - 1):
        tempArea = widthDiff * (seros[j + 1] - seros[j])
        if maxArea < tempArea:
            maxArea = tempArea
    
print(maxArea)
        


        