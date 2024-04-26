class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
   
        def generateSums(length):
            maxVal = first = sum(nums[:length])
            maxValIndex = (0,length-1)
            sums =  [(first,0,length-1)]

            for i in range(length,len(nums)):
                first -= nums[i - length]
                first += nums[i]
                if first > maxVal:
                    maxValIndex = (i-length + 1 ,i)
                    maxVal = first
                sums.append((first, i-length+1, i))
            
            return maxVal, maxValIndex, sums

        maxFirst, maxFirstIndex, firstSums  = generateSums(firstLen)
        maxSecond, maxSecondIndex, secondSums  = generateSums(secondLen)

        maxVal = 0
        for firstVal, firstStart, firstEnd in firstSums:
            for secondVal, secondStart, secondEnd in secondSums:
                if secondEnd < firstStart or secondStart > firstEnd:
                    maxVal = max(maxVal, firstVal + secondVal)

        # for val, start, end in firstSums:
        #     if end < maxSecondIndex[0] or start > maxSecondIndex[1]:
        #         maxFirstVal = max(maxFirstVal, val)


        print(firstSums, maxFirst, maxFirstIndex)
        print(secondSums, maxSecond, maxSecondIndex)


        return maxVal



