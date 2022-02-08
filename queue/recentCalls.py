class RecentCounter:

    def __init__(self):
        self.counter = []
        self.timeRange = [0, 0]

    def ping(self, t: int) -> int:

        self.timeRange[0] = t-3000
        self.timeRange[1] = t

        self.counter.append(t)

        length = len(self.counter)
        i = 0
        while i < length:

            if not (self.timeRange[0] <= self.counter[0] <= self.timeRange[1]):

                self.counter.pop(0)

            i += 1

        return len(self.counter)


obj = RecentCounter()
print(obj.ping(642))
print(obj.ping(1849))
print(obj.ping(4921))
print(obj.ping(5936))
print(obj.ping(5957))

# ["RecentCounter","ping","ping","ping","ping","ping"]
# [[],[642],[1849],[4921],[5936],[5957]]
