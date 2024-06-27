class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        count = Counter([*edges[0],*edges[1]])
        return count.most_common()[0][0]
        