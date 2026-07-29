class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0 # left pointer
        j = len(height) - 1 # right pointer 
        max = 0

        while i < j:
            if height[i] < height[j]: # handle when we are rate-limited by the left side
                vol = (j - i) * height[i]
                max = vol if vol > max else max
                i += 1 
            else: # handle when we are rate-limited by the right side / same size
                vol = (j - i) * height[j]
                max = vol if vol > max else max
                j -= 1
                
        return max




