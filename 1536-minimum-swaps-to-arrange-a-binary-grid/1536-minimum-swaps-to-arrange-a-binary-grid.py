class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        
        N = len(grid[0])
        arr = []

        # get right most 1
        for idx, row in enumerate(grid):
            i = 0
            while i < N and row[N-i-1] == 0:
                i += 1           
            arr.append(N - i - 1)

        # check valid
        for i, val in enumerate(sorted(arr)):
            if val > i:
                return -1


        swap = idx = 0
        
        # simulate swaps
        for idx in range(N):

            # idx already valid
            if arr[idx] <= idx:
                continue
            
            # find next closes valid
            target = -1
            for i, val in enumerate(arr[idx:]):
                if val <= idx:
                    target = i + idx
                    break
            else:
                print("ERR")
                return -1
            
            swap += (target - idx)
            for i in range(target, idx, -1):
                arr[i], arr[i-1] = arr[i-1], arr[i]

        return swap
            
            
        