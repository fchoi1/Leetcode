class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = defaultdict(int)
        q = math.ceil(len(arr)/4)
        split = arr[:q * 1]
        split2 = arr[q * 1:q * 2]
        split3 = arr[q * 2:q * 3]
        split4 = arr[q * 3:]
        for n in split:
            if n == split[0] or n == split[-1]:
                counts[n] +=1
        for n in split2:
            if n == split2[0] or n == split2[-1]:
                counts[n] +=1
        for n in split3:
            if n == split3[0] or n == split3[-1]:
                counts[n] +=1
        for n in split4:
            if n == split4[0] or n == split4[-1]:
                counts[n] +=1
        for key,val in counts.items():
            if val > len(arr)/4:
                return key
        return arr[0]



        