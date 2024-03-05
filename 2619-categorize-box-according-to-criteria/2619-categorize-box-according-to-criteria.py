class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume = length * width * height
        dims = [length, width, height]
        bulky = heavy = False

        if volume >= 10**9 or any(d >= 10 ** 4 for d in dims):
            bulky = True
        if mass >= 100:
            heavy = True
        
        if bulky and heavy:
            return "Both"
        elif bulky:
            return "Bulky"
        elif heavy:
            return "Heavy"
        else:
            return "Neither"
        