N, K = map(int, input().split())
num = input()
st = []

cnt = 0

for i in range(len(num)):
    # 넣기 전에, st의 top부터 보면서 자신보다 작은 숫자를 Pop한 후
    # pop할 때마다 cnt를 센다.
    while st and st[-1] < int(num[i]) and cnt < K:
        st.pop()
        cnt += 1

    # 더이상 pop할 수 없을 때 push한다.
    st.append(int(num[i]))

# K개를 다 못지웠을 경우, 가장 작은 자리 숫자부터 남은 만큼 지운다.

l = st[:len(st) - (K - cnt)]
ans = ""

for n in l:
    ans += str(n)

print(ans)




    


