class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n # There is always a line that passes through 2 points
        maxi = 1 # In starting maxi as 1 as one point always lie on a staright line 
        for ind, poi1 in enumerate(points): # Using enumerate to get index as well as the num 
            slopeM = defaultdict(int) # Making a dictionary to keep track of all types of slope 
            for j , poi2 in enumerate(points[ind+1:]): # getting x2 and y2 as point2 therefore starting from index of previous +1
                slope = self.slope(poi1,poi2) # finding the slope using point1 and 2
                slopeM[slope] += 1
                maxi = max(slopeM[slope],maxi) # Updating the maximum 
        return maxi+1

    def slope(self,x,y):
        x1, y1 = x
        x2, y2 = y
        if x1-x2 == 0:
            return 
        return (y1-y2)/(x1-x2) # Slope of a line
    
        