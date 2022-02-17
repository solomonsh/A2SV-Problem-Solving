def subarraySum(nums, k):

    sums_val = {0: 1}

    cur_sum = 0
    count = 0

    for i in range(len(nums)):
        cur_sum += nums[i]

        if cur_sum-k in sums_val:
            count += sums_val[cur_sum-k]

        if cur_sum not in sums_val:
            sums_val[cur_sum] = 1
        else:
            sums_val[cur_sum] += 1
    return count


print(subarraySum([0, 2], 2))
# print(subarraySum([0,0,0,0,0,0,0,0,0,0],0))
