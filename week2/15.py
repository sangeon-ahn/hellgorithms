import heapq, sys
input = sys.stdin.readline

N = int(input())
q1 = []
q2 = []

for _ in range(N):
    num = int(input())

    """
        최대힙, 최소힙 각각 q1, q2로 만듬
        이후, q1과 q2 크기 같으면 q1에 넣음.
        q1이 q2보다 크면 q2에 넣음
        넣기 작업 끝난 후, 양 큐의 top 비교해서, q1의 top보다 q2의 top이 더 작으면 스왑 반복
        
         -----     ------
          ---     ---------
          --   --------------
          - --------------------
    """
    
    if len(q1) == len(q2):
        heapq.heappush(q1, -num)
    
    elif len(q1) > len(q2):
        heapq.heappush(q2, num)
    
    while q1 and q2 and -q1[0] > q2[0]:
        temp1 = -heapq.heappop(q1)
        temp2 = heapq.heappop(q2)

        heapq.heappush(q1, -temp2)
        heapq.heappush(q2, temp1)
    
    print(-q1[0])
