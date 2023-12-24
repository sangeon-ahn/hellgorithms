n1 = input()
n2 = input()

ans = 0
for i in range(len(n2)):
    res = 0
    for j in range(len(n1)):
        res += int(n1[-1 - j]) * int(n2[-1 - i]) * (10**j)
    ans += res * (10 **i)
    print(res)
print(ans)