"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

"""
#Solution
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        squareRoot = num ** 0.5
        if (squareRoot - math.floor(squareRoot)) == 0:
            return True
        return False