import math
N = int(input())

for _ in range(N):
    nums = list(map(int, input().split()))
    
    heads = nums[0]
    scores = nums[1:]

    avg = sum(scores) / heads

    winners = 0
    for score in scores:
        if score > avg:
            winners += 1
    
    res = winners / heads * 100
    print("{:.3f}%".format(res))