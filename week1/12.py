T = int(input())

for _ in range(T):
    Oxes = input()

    result = 0
    conse = 1
    for i in range(len(Oxes)):
        if Oxes[i] == 'X':
            conse = 1
            continue
        
        result += conse
        conse += 1
    
    print(result)

