
class Solution:
    def sumOddLengthSubarrays(self, arr):

        total_sum = 0

        for i in range(len(arr)):

            total_sum += arr[i]
            count = 1
            subArraySum = arr[i]

            for j in range(i+1, len(arr)):
                count += 1
                subArraySum += arr[j]
                if count > 1 and count % 2 != 0:
                    total_sum += subArraySum

        return total_sum


sol = Solution()
print(sol.sumOddLengthSubarrays([1, 4, 2, 5, 3]))
