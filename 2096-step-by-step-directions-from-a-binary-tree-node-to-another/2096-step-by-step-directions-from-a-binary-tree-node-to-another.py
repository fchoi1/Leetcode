class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        dq = deque([[root, ""]])
        sourceDirections = ""
        destDirections = ""
        while len(dq) > 0:
            curr = dq.popleft()
            if curr[0] is None:
                continue
            if curr[0].val == startValue:
                sourceDirections = curr[1]
            if curr[0].val == destValue:
                destDirections = curr[1]
            dq.append([curr[0].left, curr[1]+"L"])
            dq.append([curr[0].right, curr[1]+"R"])

        index = 0
        for i in range(min(len(sourceDirections), len(destDirections))):
            if sourceDirections[i] == destDirections[i]:
                index += 1
            else:
                break
        
        return (len(sourceDirections) - index) * "U" + destDirections[index:]