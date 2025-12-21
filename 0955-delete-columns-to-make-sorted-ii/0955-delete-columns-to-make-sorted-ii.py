class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # exclude
        # how do we know 
        
        maxDelete = len(strs[0])

        inOrder = False
        excluded = -1
        
        while not inOrder:
            
            inOrder = True
            newStrs = []

            # construct strs
            for s in strs:
                newStr = ''
                for i in range(len(s)):
                    if i == excluded:
                        continue
                    newStr += s[i]
                newStrs.append(newStr)


            print("newStr", newStrs, excluded)
            for prev, curr in zip(newStrs, newStrs[1:]):
                if curr >= prev:
                    continue

                for i in range(len(curr)):
                    if curr[i] < prev[i]:
                        excluded = i
                        inOrder = False
                        break
                if not inOrder:
                    break

            # reset
            strs = newStrs
                
        return maxDelete - len(strs[0])