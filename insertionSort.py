def insertionSort(x):
    n = len(x)
    l = 0
    for i in range(1, n):
        k = x[i]
        j = i
        while j > 0 and x[j-1] > k:
            l = l +1
            x[j] = x[j-1]
            j = j - 1
        x[j] = k
    return x, l

y = [9, 8, 5, 6, 7, 3, 10, 2, 0, 4, 1] 
y = insertionSort(y)
print(y)