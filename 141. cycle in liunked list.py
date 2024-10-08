# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast= fast.next.next
            slow= slow.next
            if fast == slow:return True
        return False #o(n) o(1)
        dic={}
        while head: #o(nlog(n)) 0(n)
            if head in dic: return 1
            dic[head]=0
            head = head.next
        return 0

        
        
        