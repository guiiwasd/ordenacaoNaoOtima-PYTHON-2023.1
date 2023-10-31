def shellSort(x):
    h = 1
    n = len(x)
    while h < n:
        h = h * 3 + 1
    while h > 1:
        h = h // 3
        for i in range(h, n, h):
            atual = x[i]
            j = i - h
            while j >= 0 and atual < x[j]:
                x[j + h] = x[j]
                j = j - h
            x[j + h] = atual
    return x

y = [9, 8, 5, 6, 7, 3, 10, 2, 0, 4, 1]
y = shellSort(y)
print(y)

