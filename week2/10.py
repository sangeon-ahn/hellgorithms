import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
q = deque()

for _ in range(N):
    ops = input().split()

    command = ops[0]

    if command == "push":
        num = int(ops[1])
        q.append(num)

    elif command == "pop":
        if not q:
            print(-1)
        else:
            print(q.popleft())

    elif command == "size":
        print(len(q))

    elif command == "empty":
        if not q:
            print(1)
        else:
            print(0)

    elif command == "front":
        if not q:
            print(-1)
        else:
            print(q[0])

    elif command == "back":
        if not q:
            print(-1)
        else:
            print(q[-1])

    else:
        print("EXCEPTION")
