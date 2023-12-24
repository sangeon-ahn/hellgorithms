n1 = int(input())
n2 = int(input())
n3 = int(input())

mul = n1 * n2 * n3
strMul = str(mul)
dic = {}

for i in range(len(strMul)):
    if int(strMul[i]) not in dic:
        dic[int(strMul[i])] = 1
    else:
        dic[int(strMul[i])] += 1

for i in range(10):
    if i not in dic:
        print(0)
    else:
        print(dic[i])

