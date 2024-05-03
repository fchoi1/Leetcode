class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def build(in_order, post_order):
            if not post_order or not in_order:
                return None

            parentVal = post_order.pop()
            i = 0
            for val in in_order:
                if val == parentVal:
                    break
                i += 1

            parent = TreeNode(parentVal)
            parent.left = build(in_order[:i], post_order[:i])
            parent.right = build(in_order[i+1:], post_order[i:])
            return parent

        return build(inorder, postorder)
