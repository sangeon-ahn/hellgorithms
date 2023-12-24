import sys
input = sys.stdin.readline

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
points.sort(key = lambda p: p[0])

def getDist(idx1, idx2):
    return (points[idx1][0] - points[idx2][0])**2 + (points[idx1][1] - points[idx2][1])**2

def div_conq(st, en): # points[st] ~ points[en] 사이의 점들 중 최단 두 점 사이 거리
    if st == en:
        return sys.maxsize
    
    if en - st == 1:
        return getDist(st, en)
    
    mid = (st + en) // 2
    left = div_conq(st, mid)
    right = div_conq(mid + 1, en)

    minDist = min(left, right)

    # 이제, mid를 기준선으로 두고 거리가 2*minDist인 두 선 그리기
    # 두 선 사이의 점을 y값 기준 오름차순한 후 밑에서부터 y축 거리가 minVal보다 작은 경우에만 거리 구해서 비교
    
    newPoints = []


    # for i in range(st, en + 1):
    #     # mid - minDist < 해당 점의 x좌표 < mid + minDist
    #     if points[mid][0]**2 - minDist <= points[i][0]**2 <= points[mid][0]**2 + minDist:
    #         newPoints.append(i)

    for idx in range(st, en + 1):
        # 밴드 내에 있으면 good_points에 넣기
        if abs(points[mid][0] - points[idx][0])**2 < minDist:
            newPoints.append(idx)
    
    newPoints.sort(key = lambda x: points[x][1]) # y값 기준 오름차순

    for i in range(len(newPoints) - 1):
        for j in range(i + 1, len(newPoints)):
            if (points[newPoints[j]][1] - points[newPoints[i]][1])**2 < minDist:
                minDist = min(minDist, getDist(newPoints[j], newPoints[i]))
            else:
                break
        
    return minDist

print(div_conq(0, len(points) - 1))