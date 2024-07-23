class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [ n for h,n in sorted([(h,n) for h,n in zip(heights,names)], reverse=True) ]
        
