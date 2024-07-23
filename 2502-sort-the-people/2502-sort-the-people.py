class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
     together = [(h,n) for h,n in zip(heights,names)]
     together.sort(reverse=True)
     return [n for h,n in together ]
        
