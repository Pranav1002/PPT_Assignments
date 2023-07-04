def changeArray(arr):
    arr2 = []
    for i in range(1, len(arr), 2):
        arr2.append(arr[i])
    print(arr2)

changeArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])