# Definition for singly-linked list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def next_larger_nodes(head):
        stack = []
        result = []
        pos = 0

        while head:
            result.append(0)

            while stack and head.val > stack[-1][1]:
                idx, _ = stack.pop()
                result[idx] = head.val

            stack.append((pos, head.val))
            head = head.next
            pos += 1

        return result


list2 = ListNode(2)
list2.next = ListNode(7)
list2.next.next = ListNode(4)
list2.next.next.next = ListNode(3)
list2.next.next.next.next = ListNode(5)

sol = Solution()
print(sol.nextLargerNodes(list2))
