class Solution:
    def mySqrt(self, x: int) -> int:
        # do a loop until x 
        square = 1
        while square*square <= x:
            square += 1
        
        return square - 1