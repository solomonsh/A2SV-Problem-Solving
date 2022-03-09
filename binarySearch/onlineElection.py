from collections import Counter

class TopVotedCandidate:

    def __init__(self, persons, times):
            
            self.persons = persons
            self.times = times

    def q(self, t: int) -> int:
        
        left = 0
        right = len(self.persons)-1
        
        index = 0
        
        while left<=right:
            
            mid = left + (right-left)//2
            
            if  times[mid] == t:
                index  = mid
                break
                
            elif times[mid] >  t:
                right = mid-1
            
            elif times[mid] <  t:
                left = mid+1
            
        if left> right: index = right
 
        
        until_days_persons = self.persons[:index+1]
         
        counter = Counter(until_days_persons)
        
        maxVotes = [0,0]
        result = 0
        for key,value in counter.items():
            
           if value >= maxVotes[1]:
            if self.comesLast(maxVotes[0],key,until_days_persons) == key:
                maxVotes = [key,value]
                result = key

        print(result)
        
    def comesLast(self,val1,val2,lst):
            for i in range(len(lst)-1,-1,-1):
                if lst[i] == val1:
                    return val1
                elif lst[i] == val2:
                    return val2


# Your TopVotedCandidate object will be instantiated and called as such:
persons = [0, 1, 1, 0, 0, 1, 0] 
times  =  [0, 5, 10, 15, 20, 25, 30]
obj = TopVotedCandidate(persons, times)
param_1 = obj.q(3)
param_1 = obj.q(12)
param_1 = obj.q(25)
param_1 = obj.q(15)
param_1 = obj.q(24)
param_1 = obj.q(8)
