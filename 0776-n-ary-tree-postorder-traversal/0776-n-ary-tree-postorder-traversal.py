class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def dfs(node):
            if not node:
                return
            for child in node.children:
                dfs(child)
            ans.append(node.val)
        dfs(root)
        return ans
        