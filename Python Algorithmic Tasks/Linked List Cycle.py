from typing import Optional

# using hare and tortoise approach
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool: # type: ignore
    
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
    
        return False