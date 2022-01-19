def insertionSort1(n, arr):
    right_most = arr[-1]

    swapped = False
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > right_most:
            arr[i+1] = arr[i]

        elif arr[i] < right_most:
            arr[i+1] = right_most
            swapped = True
            break

        ars = " ".join(str(a) for a in arr)
        print(ars)

    if not swapped:
        arr[0] = right_most

    ars = " ".join(str(a) for a in arr)
    print(ars)

# insertionSort1(10,[2,3,4,5,6,7,8,9,10,1])
