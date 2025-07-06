class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):

        # n1 < n2
        self.c1 = Counter(nums1)
        self.c2 = Counter(nums2)
        self.n2 = nums2
        

    def add(self, index: int, val: int) -> None:

        old = self.n2[index]
        new = old + val
        self.c2[old] -= 1
        self.c2[new] += 1
        self.n2[index] = new

    def count(self, tot: int) -> int:
        counts = 0
        for val, c in self.c1.items():
            target = tot - val
             
            if target not in self.c2:
                continue
            
            counts += c * self.c2[target]
        return counts

        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)