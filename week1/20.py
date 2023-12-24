# 낮에 A미터 올라가고 밤에 B미터 미끄러지고 나무 높이 V미터
A, B, V = map(int, input().split())

# 일단, 낮에 올라가기만 하면 끝나는 순간을 찾기
# X >= V - A
# X = (V - A) // (A - B)

if (V - A) % (A - B) != 0:
    print((V - A) // (A - B) + 2)
else:
    print((V - A) // (A - B) + 1)






