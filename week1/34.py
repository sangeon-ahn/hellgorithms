from collections import defaultdict

heights = [int(input()) for _ in range(9)]

dic = defaultdict(bool)

hSum = 0
for h in heights:
    dic[h] = True
    hSum += h

hRest = hSum - 100

excluded = [0, 0]
for h in heights:
    if hRest - h in dic and hRest - h != h:
        excluded[0] = h
        excluded[1] = hRest - h
        break

heights.sort()

for h in heights:
    if h == excluded[0] or h == excluded[1]:
        continue
    
    print(h)

    
