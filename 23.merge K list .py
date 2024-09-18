# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # dic={}
        sortList= ListNode()
        start=sortList

        while True:
            maximum= 123456763546
            maxIndex=None

            # flag = True
            for index, x in enumerate(lists):
                if x:
                    flag=False
                    if x.val <= maximum:
                        maximum = x.val
                        maxIndex = index
            # print(maximum)
            if maxIndex is None:
                break
            sortList.next=lists[maxIndex]
            sortList = sortList.next
            lists[maxIndex] = lists[maxIndex].next 
        return start.next


            