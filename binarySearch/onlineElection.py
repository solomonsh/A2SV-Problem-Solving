 

class TopVotedCandidate:
    def __init__(self, persons, times):
        self.persons = persons
        self.times = times
        
    
    def find_index(self,t):
        left = 0 
        right = len(self.times)-1

        while left<=right:

            mid = (left+right)//2

            if t == self.times[mid]:
                return mid
            
            elif t<self.times[mid]:
                right = mid - 1
            
            elif t>self.times[mid]:
                left = mid+1

        return right

    
    def findWinner(self,c1,c2,index):

        for i in range(index,-1,-1):
            if c1 == self.persons[i]:
                return c1
            
            if c2 == self.persons[i]:
                return c2


    def q(self, t: int) -> int:
        index = self.find_index(t)
        counter = {}

        for i in range(index+1):
            if self.persons[i] in counter:
                counter[self.persons[i]] += 1
            
            else:
                counter[self.persons[i]] = 1

        sorted_counter = {k: v for k, v in sorted(counter.items(), key=lambda item: item[1],reverse=True)}
        winners = []
        i = 0
        for k,v in sorted_counter.items():
            i+=1
            if i > 2:
                break
            winners.append((k,v))

        if len(winners) < 2:
            return winners[0][0]
        else:
            if winners[0][1] == winners [1][1]:
                 return  self.findWinner(winners[0][0],winners[1][0],index)
            
            else:
                return winners[0][1]

        


 

# Your TopVotedCandidate object will be instantiated and called as such:
persons = [0, 1, 1, 0, 0, 1, 0] 
times  =  [0, 5, 10, 15, 20, 25, 30]
obj = TopVotedCandidate(persons, times)

# print(obj.find_index(23))
# param_1 = obj.q(3)
param_1 = obj.q(12)
# param_1 = obj.q(25)
# param_1 = obj.q(15)
# param_1 = obj.q(24)
# param_1 = obj.q(8)
