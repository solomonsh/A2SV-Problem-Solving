import random


class Solution:

    def __init__(self, w):
        self.w = w
        self.indeces = [i for i in range(0, len(w))]

    def pickIndex(self) -> int:

        result = random.choices(population=self.indeces,
                                k=1, weights=self.w)[0]
        return result
