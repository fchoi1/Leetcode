class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # 2d dp

        # for each index
        #
        N = len(arr)
        

        @cache
        def jump(index):
            nextIdx = []
            ans = 0

            for i in range(1, d + 1):
                
                if index + i >= N:
                    break
                
                if arr[index] <= arr[index + i]:
                    break
                
                nextIdx.append(index + i)
            
            for i in range(1, d + 1):
                
                if index - i < 0:
                    break
                
                if arr[index] <= arr[index - i]:
                    break
                
                nextIdx.append(index - i)
            
            for idx in nextIdx:
                ans = max(ans, jump(idx))

            return ans + 1
        
        most = 0
        for i in range(N):
            most = max(most, jump(i))
        
        return most

                
            