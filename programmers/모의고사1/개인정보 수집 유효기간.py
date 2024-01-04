from collections import defaultdict


def totaldays(parsedDate):
    return int(parsedDate[0]) * 12 * 28 + int(parsedDate[1]) * 28 + int(parsedDate[2])

def check(date, due, today):
    parsedDate = date.split('.')
    parsedToday = today.split('.')

    prevDays = totaldays(parsedDate)
    todayDays = totaldays(parsedToday)

    if prevDays > todayDays:
        return True
    
    diff = todayDays - prevDays

    if diff >= due * 28:
        return True

    return False

def solution(today, terms, privacies):
    answer = []
    termsDict = defaultdict(int)

    for t in terms:
        info = t.split()
        termsDict[t[0]] = int(info[1])

    for idx, privacy in enumerate(privacies):
        date, tp = privacy.split()

        if tp not in termsDict:
            continue

        if check(date, termsDict[tp], today):
            answer.append(idx + 1)
    
    answer.sort()
        
    return answer


today= "2020.01.01"
terms = 	["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

sol = solution(today, terms, privacies)
print(sol)