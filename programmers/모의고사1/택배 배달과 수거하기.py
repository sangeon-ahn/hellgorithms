def solution(cap, n, deliveries, pickups):
    answer = 0
    
    capTemp = cap
    """
    일단, 매 타임마다 왕복 거리 = max(배달 or 수거) * 2
    매 타임마다, cap 기준으로 배달 줄여나가고, cap 기준으로 수거 줄여나감. 줄이기 전, 두 배달 수거 중 0이 아닌 집의 최대 거리를 구함.
    """

    while deliveries or pickups:
        dist = 0

        deliCap = cap
        while deliCap > 0:
            if not deliveries:
                break

            if deliveries[-1] == 0:
                deliveries.pop()
            else:
                dist = max(dist, len(deliveries))
                
                if deliCap >= deliveries[-1]:
                    deliCap -= deliveries[-1]
                    deliveries.pop()
                else:
                    deliveries[-1] -= deliCap
                    break
        
        pickCap = cap
        while pickCap > 0:
            if not pickups:
                break

            if pickups[-1] == 0:
                pickups.pop()
            else:
                dist = max(dist, len(pickups))

                if pickCap >= pickups[-1]:
                    pickCap -= pickups[-1]
                    pickups.pop()
                else:
                    pickups[-1] -= pickCap
                    break
        
        answer += dist * 2    

    return answer

cap	 = 4
n = 5
deliveries= [1, 0, 3, 1, 2]
pickups	= [0, 3, 0, 4, 0]

sol = solution(cap, n, deliveries, pickups)
print(sol)