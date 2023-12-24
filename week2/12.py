from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
q = deque([i for i in range(1, N + 1)])
store = deque()

while q:
    for i in range(K - 1):
        q.append(q.popleft())
    store.append(q.popleft())

print("<", end='')

for i in range(len(store) - 1):
    print(store[i], end=', ')

print(store[-1], end= '>')


