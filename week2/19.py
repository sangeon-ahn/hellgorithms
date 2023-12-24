import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
nums = []

def postOrder(st, en):
    if st > en:
        return
    
    head = nums[st]
    div = en + 1
    for i in range(st + 1, en + 1):
        if head < nums[i]:
            div = i
            break
    
    postOrder(st + 1, div - 1)
    postOrder(div, en)
    print(head)

# 엔터 들어올 때까지 입력
while True:
    try:
        nums.append(int(input().rstrip()))
    except:
        break

postOrder(0, len(nums) - 1)
