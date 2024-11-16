class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
  
        arr = []
        count = 1
        prev = None

        for i, n in enumerate(nums):
            if prev and n == prev + 1:
                count += 1
            else:
                count = 1

            if i + 1 >= k:
                if count >= k:
                    arr.append(n)
                else:
                    arr.append(-1)
            prev = n

        return arr
