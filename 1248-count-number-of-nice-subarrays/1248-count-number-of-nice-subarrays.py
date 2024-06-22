class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        l = 0
        total = 0
        oddCount = 0
        evenRight = evenLeft = 0
        reset=False
        for i,n in enumerate(nums):

            if n % 2 == 1:
                oddCount += 1
                reset = True
            else:
                evenRight += 1
            # print(i,total, "oddcount",n, oddCount, "evenRight",evenRight)
            evenLeft = 1
            while l < i and oddCount > k:
                # print("total add", evenRight)
                total += evenRight
                if nums[l] % 2 == 1:
                    oddCount-=1
                    l+=1
                    break
                l += 1
            if reset:
                evenRight = 1
                reset = False

            # if oddCount == k:
            #     print(l,"adddin at",i,n, "val",evenLeft,  evenRight)
            #     total +=  evenLeft * evenRight 
        print(oddCount, l, i)
        while l <= i and oddCount >= k:
            total += evenRight
            # print("total after add", evenRight)

            if nums[l] % 2 == 1:
                oddCount-=1
                l += 1
                break
            # evenLeft += 1
            l += 1
        # print("done", total, 'l', l)
        # left count, right count 
        return total

        # 1 1 2 1 1 2 2 2 