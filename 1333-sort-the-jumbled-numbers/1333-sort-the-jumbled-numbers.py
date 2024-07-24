class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def transform(number):
            new = 0
            for i,n in enumerate(str(number)[::-1]):
                new += mapping[int(n)] * 10 ** i
            return new
        
        ans = []
        for i,n in enumerate(nums):
            ans.append((transform(n),i, n)) 
            
        ans.sort()
        return [x[2] for x in ans]

            

        