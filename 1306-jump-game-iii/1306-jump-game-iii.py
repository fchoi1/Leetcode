class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        N = len(arr)
        self.seen = set()
        
        def jump(index):
            if index in self.seen:
                return False
            self.seen.add(index)
                
            if index >= N or index < 0:
                return False

            if arr[index] == 0:
                return True

            return jump(index + arr[index]) or jump(index - arr[index])

        return jump(start)