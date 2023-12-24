import sys
from collections import deque
N = int(input())

if N == 1:
    print(1)
    sys.exit()

q = deque([i for i in range(1, N + 1)])

while len(q) > 2:
    q.popleft()
    
    num = q.popleft()
    q.append(num)

print(q[1])
