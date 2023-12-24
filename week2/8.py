import sys
input = sys.stdin.readline

N = int(input())
circles = [list(map(int, input().split())) for _ in range(N)]

# 1. 오른쪽 끝 점 기준 오름차순 정렬. 같은 경우, 왼쪽 끝점이 큰게 먼저 나오도록.
circles.sort(key = lambda circle : (circle[0] + circle[1], -(circle[0] - circle[1])))

# 2. 스택 생성. 들어갈 값 타입: (오른쪽 점, 왼쪽 점)
st = []

ans = len(circles) + 1
# 원을 딱 뒀는데, 내부에 원들이 접해서 영역이 2개로 나뉘어짐 -> 2개 영역 생성. 그 외 -> 1개 영역 생성.
# 3. circles 돌면서 st 확인.
for circle in circles: # (중심좌표, 반지름)
    curRight = circle[0] + circle[1] # 현재 접해야 하는 지점.

    # st에는 자기보다 끝점이 같거나 작은 애들만 있음.
    while st:
        innerCircle = st.pop() # 내부 원 뽑아서,

        # 자신의 안에 있을 때, 바깥에 있을 때로 구분.
        # 안에 있을 때,
        if innerCircle[0] - innerCircle[1] >= circle[0] - circle[1]:
            # 오른쪽과 접할 때,
            if innerCircle[0] + innerCircle[1] == curRight:
                # 왼쪽과도 접할 때,
                if innerCircle[0] - innerCircle[1] == circle[0] - circle[1]:
                    ans += 1
                    break
                # 왼쪽이랑 안접하면,
                else:
                    # 새롭게 접해야 할 지점 업데이트
                    curRight = innerCircle[0] - innerCircle[1]
        
        # 바깥에 있을 때,
        else:
            st.append(innerCircle)
            break
    
    st.append(circle)

print(ans)
        
        
        



