class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 2 # This is the end of the array 
        j = len(nums) - 1 # This will be the end of the sliding window
        while i >= 0:
            if nums[i] >= (j - i): # the max jump length is greater/equal to the distance
                j = i
                i -= 1
            else: # max jump is smaller
                i -= 1
        return j == 0
        