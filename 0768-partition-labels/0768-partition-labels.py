class Solution:
    def partitionLabels(self, s: str) -> List[int]:
       
        last = {char: i for i, char in enumerate(s)}
        part = []
        index = end = -1
        
        for i,char in enumerate(s):
            end = max(end, last[char])
            if i == end:
                part.append(i - index)
                index = i
        
        return part
        