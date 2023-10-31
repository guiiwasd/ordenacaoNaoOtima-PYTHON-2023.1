def bubbleSort(x):
    n = len(x)
    print("vetor original: ", x)
    for i in range(0, n-1):
        ordenado = True
        for j in range(n-1, i, -1):
            if x[j] < x[j-1]:
                x[j], x[j-1] = x[j-1], x[j]
                ordenado = False
        print(i, "vetor: ", x)
        if ordenado:
            break

y = [9, 8, 5, 6, 7, 3, 10, 2, 0, 4, 1]
y = bubbleSort(y)
print(y)
