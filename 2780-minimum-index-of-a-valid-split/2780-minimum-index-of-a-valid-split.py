class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # divide and check?
        # preprocess

        # dominant needs more than half?

        N =  len(nums)
        max_val, max_count = Counter(nums).most_common(1)[0]
        if max_count <= N // 2:
            return -1

        print(max_val, max_count)

        curr_count = 0
        for i,n in enumerate(nums):
        
            if n == max_val:
                curr_count += 1

            # print(curr_count, (i+1)//2 , ":", max_count - curr_count, (N - i  + 1) // 2, "index", i)
            if curr_count > (i+1)// 2 and max_count - curr_count >= (N - i + 1) // 2:
                return i 
            

        return -1