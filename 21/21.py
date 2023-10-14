class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = out = ListNode()

        while list1 and list2:

            if list1.val > list2.val:
                out.next = list2
                list2 = list2.next
            else:
                out.next = list1
                list1 = list1.next
            
            out = out.next
        
        out.next = list1 if list1 else list2
        
        return head.next