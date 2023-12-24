import sys
input = sys.stdin.readline

K = int(input())
nums = [int(input()) for _ in range(K)]

st = []

for n in nums:
    if n == 0:
        st.pop()
    else:
        st.append(n)

print(sum(st))