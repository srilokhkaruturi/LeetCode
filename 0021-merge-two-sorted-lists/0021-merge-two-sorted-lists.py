# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize dummy and current pointer
        dummy = ListNode(-1)
        current = dummy
        
        # While both lists are not empty
        while list1 and list2:
            # Compare the values of list1 and list2
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            # Move to the next position in the merged list
            current = current.next
        
        # If one of the lists is not empty, attach it to the end
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        # Return the merged list starting from the next of dummy node
        return dummy.next