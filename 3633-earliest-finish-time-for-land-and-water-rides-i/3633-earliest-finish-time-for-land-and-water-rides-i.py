class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        earliest = inf
        for ls, ld in zip(landStartTime, landDuration):
            for ws, wd in zip(waterStartTime, waterDuration):
                if ls > ws:
                    if ls < ws + wd:
                        earliest = min(earliest, ws + ld + wd)
                    else:
                        earliest = min(earliest, ls + ld)
                else:
                    if ws < ls + ld:
                        earliest = min(earliest, ls + ld + wd)
                    else:
                        earliest = min(earliest, ws + wd)
        return earliest