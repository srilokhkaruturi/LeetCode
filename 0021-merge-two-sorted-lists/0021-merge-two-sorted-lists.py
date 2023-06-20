# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        
        head = ListNode()
        
        pointer = head
        pointer_one = list1
        pointer_two = list2
        
        while pointer_one and pointer_two:
            print(pointer_one.val, pointer_two.val)
            
            if pointer_one.val == pointer_two.val:
                pointer.next = ListNode(pointer_one.val)
                pointer = pointer.next
                
                pointer.next = ListNode(pointer_two.val)
                pointer = pointer.next
                
                pointer_one = pointer_one.next
                pointer_two = pointer_two.next
               
            elif pointer_one.val < pointer_two.val:
                pointer.next = ListNode(pointer_one.val)
                pointer = pointer.next
                
                pointer_one = pointer_one.next

              
            elif pointer_one.val > pointer_two.val:                
                pointer.next = ListNode(pointer_two.val)
                pointer = pointer.next
            
                pointer_two = pointer_two.next
                
                
        # check if one is null
        if not pointer_one:
            pointer.next = pointer_two
        if not pointer_two:
            pointer.next = pointer_one
            
                
        return head.next
                