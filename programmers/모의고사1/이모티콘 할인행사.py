Users = []
Emoticons = []
temp = []
discounts = [0.1, 0.2, 0.3, 0.4]
Answer = [-1, -1]
def dfs(order, n):
    global discounts, Users, Emoticons, Answer, temp
    if order == n: # 할인율 다 결정됐으면,
        tmp = [0, 0]
        for user in Users:
            costs = 0
            for idx, emo in enumerate(Emoticons):
                if user[0] <= discounts[temp[idx]]*100:
                    costs += int(emo * (1 - discounts[temp[idx]]))

            if costs < user[1]:
                tmp[1] += costs
            else:
                tmp[0] += 1
        
        if Answer[0] < tmp[0]:
            Answer = tmp
        elif Answer[0] == tmp[0] and Answer[1] < tmp[1]:
            Answer = tmp
        
        return
    
    for i in range(4):
        temp.append(i)
        dfs(order + 1, n)
        temp.pop()
        
                    


def solution(users, emoticons):
    global Users, Emoticons
    Users = users
    Emoticons = emoticons

    """
        유저들이 있고, 이모티콘들이 있다.
        유저 하나에 대해 모든 (이모티콘, 할인)을 순회해서 결과를 얻는다.
        이후, 총액 >= 기준치면 구매 철회 + 서비스 가입
        일단, 4개의 할인정책, n개의 이모티콘 -> 순열 문제()
        순열 다 구한 후, 확인
        순열은 할인율 배열에 넣고 빼는 방식으로 구현
    """
    
    dfs(0, len(Emoticons)) # (결정된 할인 개수, 이모티콘 개수)

    return Answer

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
sol = solution(users, emoticons)
print(sol)