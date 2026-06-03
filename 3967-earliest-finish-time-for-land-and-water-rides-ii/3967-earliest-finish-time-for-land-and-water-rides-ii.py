class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        land_end = min(s + d for s, d in zip(landStartTime, landDuration))
        water_end = min(s + d for s, d in zip(waterStartTime, waterDuration))
        
        earliest = inf
        # check land
        for s,d in zip(waterStartTime, waterDuration):
            if s <= land_end:
                earliest = min(earliest, land_end + d)
            else:
                earliest = min(earliest, s + d)

        for s,d in zip(landStartTime, landDuration):
            if s <= water_end:
                earliest = min(earliest, water_end + d)
            else:
                earliest = min(earliest, s + d)

        
        return earliest