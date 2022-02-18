import random


class Solution:

    def __init__(self, w):
        self.w = w
        self.indeces = [i for i in range(0, len(w))]

    def pickIndex(self) -> int:

        result = random.choices(population=self.indeces,
                                k=2, weights=self.w)
        print(result)
        return result



obj = Solution([1,3])
param_1 = obj.pickIndex()