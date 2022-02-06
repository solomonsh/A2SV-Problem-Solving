from collections import Counter

class Solution:

    def removeDuplicateLetters(self, s):
        char_counter = Counter(s)
        stack = []

        seen = set()

        for char in s:
            char_counter[char] -= 1

            if char in seen:
                continue
            
        
            while stack and  char < stack[-1] and char_counter[stack[-1]] > 0:
                    popped_element  = stack.pop()
                    seen.remove(popped_element)

            stack.append(char)
            seen.add(char)

    
        return "".join(stack)