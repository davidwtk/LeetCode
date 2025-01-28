# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = newhead = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                newhead.next = list1
                list1 = list1.next
            else:
                newhead.next = list2
                list2 = list2.next
            newhead = newhead.next
        
        newhead.next = list1 or list2
        return dummy.next

        #if list1 is None:
        #    return list2
        #if list2 is None:
        #    return list1
        
        #if list1.val <= list2.val:
        #    list1.next = self.mergeTwoLists(list1.next, list2)
        #    return list1
        #else:
        #    list2.next = self.mergeTwoLists(list1, list2.next)
        #    return list2