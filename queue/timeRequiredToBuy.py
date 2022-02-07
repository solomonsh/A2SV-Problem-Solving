class Solution:
    def timeRequiredToBuy(self, tickets,k):
        queue = tickets
        
        count = 0
        i = 0
        while  queue[k]!=0:
            if queue[i] != 0:
                queue[i] -=1
                count +=1
            
            if i == len(queue)-1:
                i = 0
            
            else:
                i+=1
                
        return count
            
            