x, y, w, h = map(int, input().split())

widthMin = min(w - x, x)
heightMin = min(y, h - y)

print(min(widthMin, heightMin))
