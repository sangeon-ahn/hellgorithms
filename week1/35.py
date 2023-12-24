N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
ans = 0

for i in range(len(nums)):
    remained = M - nums[i]

    left = i + 1
    right = len(nums) - 1

    while left < right:
        twoSum = nums[left] + nums[right]

        if twoSum > remained:
            right -= 1
        else:
            ans = max(ans, twoSum + nums[i])
            left += 1

print(ans)



