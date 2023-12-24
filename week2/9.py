import sys
input = sys.stdin.readline
heights = []

def div_conq(st, en): # st ~ en 사이의 직사각형에 대해 최대 넓이를 반환하는 함수.
    if st == en:
        return heights[st]
    
    if en - st == 1:
        return max(max(heights[st], heights[en]), min(heights[st], heights[en]) * 2)
    
    mid = (st + en) // 2    
    max_area = max(div_conq(st, mid), div_conq(mid + 1, en))

    # 이제, 가운데에서부터 양쪽으로 확장해가면서 넓이 구하기
    left = mid
    right = mid + 1

    height = min(heights[left], heights[right])
    total_max = max(heights[left], heights[right], height * 2)

    # 이제 p1이나 p2가 st나 en을 모두 넘기 전까지는 while을 돌린다.
    while st < left or right < en:
        # p1을 움직이고 싶을 때는 p1이 아직 안온 상태에서 p2가 먼저 도착한 상태거나 heights[p1 - 1] > heights[p2 - 1]일 때 가능하다. 최대한 큰쪽을 계속 선택해야 최대 넓이를 구할 수 있다.
        if st < left and (right >= en or heights[left - 1] > heights[right + 1]):
            height = min(height, heights[left - 1])
            left -= 1
        else:
            height = min(height, heights[right + 1])
            right += 1
            
        total_max = max(total_max, height * (right - left + 1))

    max_area = max(max_area, total_max)
    return max_area

while True:
    TC = list(map(int, input().split()))
    N = TC[0]
    if N == 0:
        break

    heights = TC[1:]
    print(div_conq(0, len(heights) - 1))