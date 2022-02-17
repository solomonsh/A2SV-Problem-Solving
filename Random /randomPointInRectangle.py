import random


class Solution:

    def __init__(self, rects):
        self.rects = rects

        self.weights = []
        for rect in rects:
            x1, y1, x2, y2 = rect
            area = (x2-x1+1)*(y2-y1+1)
            self.weights.append(area)

        self.weights = [(x2-x1+1)*(y2-y1+1) for x1, y1, x2, y2 in rects]

        sum_of_weights = sum(self.weights)

        self.weights = [x/sum_of_weights for x in self.weights]

    def pick(self):
        rect = random.choices(
            population=self.rects,
            weights=self.weights,
            k=1
        )[0] # random.choices returns a list, we extract the first (and only) element.
        
        x1, y1, x2, y2 = rect   

        rnd_x = random.randint(x1, x2)
        rnd_y = random.randint(y1, y2)
        return [rnd_x, rnd_y]


sol = Solution([[-2, -2, 1, 1], [2, 2, 4, 6]])


print(sol.pick())
