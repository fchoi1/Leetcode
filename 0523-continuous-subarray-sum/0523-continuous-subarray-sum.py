from collections import defaultdict

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        # x = n  * k
        
        # sum % k == 0
          #return true

        remain = defaultdict(int) 
        remain[0] = -1
        sum = 0
        for i,n in enumerate(nums): 
          #print(remain, sum)
              
          sum += n
          r = sum % k 

          if r not in remain: 
            remain[r] = i
            
          elif i - remain[r] > 1:
            return True

          
        return False
      
        
    