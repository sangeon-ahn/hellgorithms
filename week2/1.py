import sys
input = sys.stdin.readline

N = int(input())
st = []

for _ in range(N):
    ops = input().split()

    command = ops[0]

    if command == "push":
        num = int(ops[1])
        st.append(num)

    elif command == "top":
        if st:
            print(st[-1])
        else:
            print(-1)

    elif command == "size":
        print(len(st))

    elif command == "empty":
        if st:
            print(0)
        else:
            print(1)

    elif command == "pop":
        if st:
            print(st.pop())
        else:
            print(-1)
    else:
        print("ERROR")