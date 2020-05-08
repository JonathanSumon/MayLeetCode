"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] 
represents the coordinate of a point. 

Check if these points make a straight line in the XY plane.
"""

#Solution

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[:2]
        for i in range(2, len(coordinates)):
            (x, y) = coordinates[i]
            if((y2 - y1) * (x1 - x) != (y1 - y) * (x2 - x1)):
                return False
        return True		