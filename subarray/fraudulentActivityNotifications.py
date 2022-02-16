
from collections import deque


def calculateMedian(counting, d):

    odd = False if d % 2 == 0 else True

    counter = 0
    index = 0

    firstMedain = 0
    secondMedain = 0

    j = 0
    while j < len(counting):

        counter += counting[j]

        if odd and counter >= d//2+1:
            firstMedain = index
            secondMedain = index
            break

        if not odd and not firstMedain and counter >= d//2:
            firstMedain = index

        if not odd and counter >= d//2+1:
            secondMedain = index
            break

        index += 1
        j += 1

    return (firstMedain+secondMedain)/2


def activityNotifications(expenditure, d):
    counting = [0]*(max(expenditure)+1)

    queue = deque()

    if d == len(expenditure):
        return 0
    count = 0
    for index, expense in enumerate(expenditure):
        if index < d:
            counting[expenditure[index]] += 1
            queue.append(expenditure[index])
        else:

            if expense >= 2*calculateMedian(counting, d):
                count += 1

            counting[queue.popleft()] -= 1
            queue.append(expenditure[index])

            counting[expenditure[index]] += 1

    return count


print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))
print(activityNotifications([1, 2, 3, 4, 4], 4))
print(activityNotifications([10, 20, 30, 40, 50], 3))
