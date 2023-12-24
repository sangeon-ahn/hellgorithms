from collections import defaultdict
N = int(input())

dic = defaultdict(int)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    if n in dic:
        return dic[n]
    
    dic[n] = n * factorial(n - 1)
    
    return dic[n]

print(factorial(N))
    