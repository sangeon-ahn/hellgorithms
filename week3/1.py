from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input().rstrip())


cache = defaultdict(int)

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    if n in cache:
        return cache[n]
    
    res = fibo(n - 1) + fibo(n - 2)
    cache[n] = res

    return res

print(fibo(N))