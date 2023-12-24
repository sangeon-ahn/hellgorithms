n1, n2 = input().split()

n1R = int(n1[::-1])
n2R = int(n2[::-1])

print(n1R if n1R > n2R else n2R)