class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # bubble sorting
        
        N = len(grid[0])
        counts = defaultdict(int)
        idxList = list(range(N))
        arr = []
 
        for idx, row in enumerate(grid):
            i = 0
            while i < N and row[N-i-1] == 0:
                i += 1           
            arr.append(N - i - 1)

        # check valid
        for i, val in enumerate(sorted(arr)):
            if val > i:
                return -1


        swap = 0
        idx = 0

        for idx in range(N):
            # valid
            if arr[idx] <= idx:
                continue
            
            # find closes valid
            target = -1
            for i, val in enumerate(arr[idx:]):
                if val <= idx:
                    target = i + idx
                    break
            else:
                print("ERR")
                return -1
            
            swap += (target - idx)
            arr = arr[:idx] + arr[target:target + 1] + arr[idx:target] + arr[target + 1:]


        return swap
            
            
        