import sys, bisect
input = sys.stdin.readline

M, N, L = map(int, input().split())
shoots = list(map(int, input().split()))
shoots.sort()
animals = [list(map(int, input().split())) for _ in range(N)]

# 1. 각 동물을 순회(for)하며, 동물의 사이에 있는 사대들을 찾는다(이분탐색).
# 2. 왼쪽 오른쪽 사대 중 사정거리 L 안에 위치하면 해당 동물은 잡을 수 있다.

ans = 0
for animal in animals:
    idx = bisect.bisect_left(shoots, animal[0]) # shoots에서 animal[0]이 몇번째 인덱스에 들어가야 정렬되는지 알려줌

    for i in [idx - 1, idx, idx + 1]: # i로 사대 접근할거임.
        if i < 0 or i >= len(shoots):
            continue

        # 거리 확인
        dist = abs(shoots[i] - animal[0]) + animal[1]

        if dist <= L:
            ans += 1
            break

print(ans)