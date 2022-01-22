from collections import Counter


class Solution:
    def minSetSize(self, arr):
        arr_counter = Counter(arr)

        sorted_counter = {k: v for k, v in sorted(
            arr_counter.items(), key=lambda item: item[1], reverse=True)}

        acc_sum = 0
        acc_count = 0

        for i, n in sorted_counter.items():
            if acc_sum >= len(arr)//2:
                return acc_count
            else:
                acc_count += 1
                acc_sum += n

        return acc_count


sol = Solution()

print(sol.minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))
