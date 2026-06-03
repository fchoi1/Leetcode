class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        land = sorted(zip(landStartTime, landDuration), key=sum)
        water = sorted(zip(waterStartTime, waterDuration), key=sum)
        earliest = inf
        # check land
        end = land[0][0] + land[0][1] 
        for s,d in water:
            if s <= end:
                earliest = min(earliest, end + d)
            else:
                earliest = min(earliest, s + d)
        # check water
        end = water[0][0] + water[0][1]
        for s,d in land:
            if s <= end:
                earliest = min(earliest, end + d)
            else:
                earliest = min(earliest, s + d)

        
        return earliest