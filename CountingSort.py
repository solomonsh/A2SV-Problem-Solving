
# Counting sort part1
# Time complexity k, where k is 100
# Space complexity k, where k is 100

def countingSort1(arr):
    counts = [0]*100

    for ar in arr:
        counts[ar] += 1

    return counts


# Counting Sort
# Time complexity n+k, where k is maximum number in the list
# Space complexity n+k, where k is the maximum number in the list

def countingSort(arr):
    counts = [0] * (max(arr)+1)

    for ar in arr:
        counts[ar] += 1

    result = []
    for i, value in enumerate(counts):
        if value != 0:
            result += [i]*value

    return result


print(countingSort([1, 0, 3, 2, 1]))
