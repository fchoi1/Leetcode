class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 2 most

        # 1 1 1 1 2 2 2 3
        people.sort()
        l,r = 0, len(people) - 1
        boat = 0
        while l < r:
            if people[r] + people[l] > limit:
                boat += 1
                r -= 1
            else:
                boat += 1
                r -= 1
                l += 1
        

        return boat if l != r else boat + 1