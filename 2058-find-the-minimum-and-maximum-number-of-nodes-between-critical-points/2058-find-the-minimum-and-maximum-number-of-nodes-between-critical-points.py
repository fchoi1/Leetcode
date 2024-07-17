# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first = curr = None
        shortest = inf

        p,c,n = head, head.next, head.next.next
        i = 1
        while n:
            if (p.val < c.val and n.val < c.val) or (p.val > c.val and n.val > c.val):
                if not first:
                    first = i
                else:
                    if not curr:
                        shortest = i - first
                    else:
                        shortest = min(shortest, i - curr)
                    curr = i
            i += 1
            p = p.next
            c = c.next
            n = n.next

        print(first, curr)
        if first == curr or curr == None:
            return [-1, -1]
        
        return [shortest, curr - first]
        