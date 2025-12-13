class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        
        valid = []
        for c, b, active in zip(code, businessLine, isActive):
            if not active or b not in ("electronics", "grocery", "pharmacy", "restaurant") or not c:
                continue
            
            updatedC = c.replace('_', '')
            
            if updatedC.isalnum() or not updatedC:
                valid.append((c,b))

        valid.sort(key=lambda x:(x[1],x[0]))

        return [x[0] for x in valid]