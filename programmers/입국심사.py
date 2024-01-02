def solve(t, times, n):
    res = 0

    for time in times:
        res += t // time
    
    return res

def solution(n, times):
    answer = float('inf')
    
    minTime = 1
    maxTime = 1e9

    while minTime <= maxTime:
        midTime = (minTime + maxTime) // 2
        print(midTime)
        val = solve(midTime, times, n)

        if val >= n:
            answer = min(answer, midTime)
            maxTime = midTime - 1
        else:
            minTime = midTime + 1

    return int(answer)

n = 6
times = [7, 10]

sol = solution(n, times)
print(sol)