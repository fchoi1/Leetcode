class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        latest = i = 0
        seen = set()
        for bus in buses:
            count = 0
            while i < len(passengers) and passengers[i] <= bus and count < capacity:
                seen.add(passengers[i])
                i += 1
                count += 1
            if count < capacity:
                latest = bus
            else:
                latest = passengers[i-1] 
            check = i-1
            while latest == passengers[check]:
                latest -= 1
                check -= 1
        return latest 


            
