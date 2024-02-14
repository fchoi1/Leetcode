class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        slow = 0
        count = 0
        for i in range(len(nums)):
            
            if nums[i] == prev:
                count += 1
                if count > 1:    
                    continue 
            else:
                count = 0      
            prev = nums[i]
            nums[slow] = nums[i]
            slow += 1
          
        return slow
        
        