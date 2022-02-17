import random


class Solution:

    def __init__(self, w):

        self.weights = [weight/sum(w) for weight in w]
        self.indeces = [i for i in range(0, len(w))]

    def pickIndex(self) -> int:

        result = random.choices(population=self.indeces,k=1, weights=self.weights)[0]
        return result
