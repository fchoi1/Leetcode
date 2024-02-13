class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        s=0
        print(d)
        for i in d:
            k=d[i]
            if k==1:
                return -1
            s+=k//3
            k=k%3
            if k!=0:
                s+=1
        return s       