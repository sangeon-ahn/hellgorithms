N = int(input())
Words = list(set([input() for _ in range(N)]))

Words.sort(key = lambda x: (len(x), x))

for word in Words:
    print(word)
