# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # reverse last half?
        ans = 0
        N = 0
        curr = head

        while curr:
            N += 1
            curr = curr.next

        mid = N // 2

        curr = head
        for _ in range(mid):
            curr = curr.next

        # reverse
        end = None
        for _ in range(mid):
            temp = curr.next
            curr.next = end
            end = curr
            curr = temp
        

        curr = head
        for _ in range(mid):
            ans = max(ans, end.val + curr.val)
            curr = curr.next
            end = end.next
            
        return ans
