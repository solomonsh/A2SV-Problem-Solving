from collections import deque

class Solution:
    def canReach(self, arr, start):

        queue = deque([start])
        visisted = set([start])


        while queue:

            current = queue.popleft()
          

            if arr[current] == 0:
                return True
            
            if (0 <= current+arr[current] <= len(arr)-1) and ((current + arr[current]) not in visisted):
                queue.append(current+arr[current])
                visisted.add(current+arr[current])

            if (0 <= current-arr[current] <= len(arr)-1) and ((current - arr[current]) not in visisted):
                queue.append(current-arr[current])
                visisted.add(current-arr[current])
        

        return False

sol = Solution() 