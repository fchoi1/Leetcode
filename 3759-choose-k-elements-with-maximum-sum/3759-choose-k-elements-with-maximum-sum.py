class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # heap?
        minN1 = min(nums1)
        order = [(n1, i) for i,n1 in enumerate(nums1)]
        
        order.sort()
        ans = []
        max_heap = []
        prev = None
        currSum = 0
        
        for n1, i in order:
            if not ans or n1 == minN1:
                ans.append((0, i))
            elif prev and prev == n1:
                ans.append((ans[-1][0], i))
            else:
                ans.append((currSum, i))
                
            if i < len(nums2):
                currSum += nums2[i]
                heapq.heappush(max_heap, nums2[i])
                if len(max_heap) > k:
                    currSum -= heappop(max_heap)
            prev = n1

        ans.sort(key=lambda x: x[1])
        return [col[0] for col in ans]
            