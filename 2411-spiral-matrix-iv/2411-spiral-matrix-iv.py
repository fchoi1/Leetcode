# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        curr = head
        for i in range(m // 2 + 1):
            # top
            for x in range(i, n-i):
                if not curr:
                    return matrix
                matrix[i][x] = curr.val
                curr = curr.next

            # right
            for y in range(i + 1, m-i):
                if not curr:
                    return matrix
                matrix[y][-i-1] = curr.val
                curr = curr.next

            # bottom
            for x in range(n-i-2, i-1, -1):
                if not curr:
                    return matrix
                matrix[-i-1][x] = curr.val
                curr = curr.next

            # left
            for y in range(m-i-2, i, -1):
                if not curr:
                    return matrix
                matrix[y][i] = curr.val
                curr = curr.next

        return matrix
        