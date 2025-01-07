class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        def getPrefix(arr):
        
            moves = sum(i if arr[i] == "1" else 0 for i in range(len(arr)))
            ones = arr.count('1')
            prefix = [moves]
            for b in arr:
                if b == "1":
                    ones -= 1
                moves -= ones
                moves = max(0, moves)
                prefix.append(moves)
            return prefix

        p_s = getPrefix(boxes)
        p_e = getPrefix(boxes[::-1])
        ans = []
 
        for a,b in zip(p_s, p_e[::-1][1:]):
            print(a + b)
            ans.append(a+b)
        return ans