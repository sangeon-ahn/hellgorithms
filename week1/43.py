N = int(input())
nums = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

nums.sort()

for target in targets:
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if target > nums[mid]:
            l = mid + 1
        elif target < nums[mid]:
            r = mid - 1
        else:
            print(1)
            break
    
    if l > r:
        print(0)