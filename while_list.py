item = []
n = 1
while True:
    if n >= 1:
        n = int(input())
        item.append(n)
    else:
        item.remove(0)
        break
print(item)
    