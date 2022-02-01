class Solution:

    # Approach 1
    def threeSumClosest(self, nums, target):

        temp = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                threeSum = a+nums[left]+nums[right]

                if threeSum > target:
                    temp.append(threeSum)
                    right -= 1

                elif threeSum < target:
                    temp.append(threeSum)
                    left += 1
                else:
                    result_sum = a+nums[left]+nums[right]
                    return result_sum

        min_difference = abs(target-temp[0])
        diff_dict = {min_difference: temp[0]}

        for n in temp[1:]:
            difference = abs(target-n)

            if difference <= min_difference:
                min_difference = difference
                diff_dict[min_difference] = n

        return diff_dict[min_difference]


# Approach 2

    def threeSumClosest(self, nums, target):

        nums.sort()
        result = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left, right = i+1, len(nums) - 1
            while left < right: 
                sum = nums[i] + nums[left] + nums[right]
                if sum == target:
                    return sum

                if abs(sum - target) < abs(result - target):
                    result = sum

                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1

        return result



sol = Solution()

print(sol.threeSumClosest([1, 2, 5, 10, 11], 12))
