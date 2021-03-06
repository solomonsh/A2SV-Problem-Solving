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


# Complete insertion sort
# Time complexity N^2
# Space complexity N

def insertionSort(arr):

    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:

            j = i
            while j > 0:
                if arr[j-1] <= arr[j]:
                    break
                else:
                    arr[j], arr[j-1] = arr[j-1], arr[j]

                j -= 1

    return arr


print(insertionSort([2, 4, -5, 6, 7, -8, 9, 10, 1]))

print(insertionSort([0, 2, -4]))
