class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        power = 0

        for n in batteryPercentages:
            if n > power:
                power += 1
        return power