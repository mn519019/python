# This algorithm requires to use two pointers to find the n difference
# from the dummy node vs the current right node after the loop.
# Topic: LinkedList

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy # dummy node
        right = head # actual listnode

        while n > 0 and right:
            right = right.next
            n -= 1
            
        while right:
            left = left.next
            right = right.next 
        
        left.next = left.next.next
        return dummy.next

    
