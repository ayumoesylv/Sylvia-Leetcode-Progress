class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 # left ptr: nums[:left) is less than the target
        right = len(nums) # right ptr: nums[right:] is greater than the target
        # calculate mid point 
        mid = left + (right - left) // 2 # nums[mid] is the next number to check
        while left < right:
            if nums[mid] < target: # increment left
                left = mid + 1
            elif nums[mid] > target: # increment right 
                right = mid 
            else: # mid is target
                return mid 
            mid = left + (right - left) // 2
        return mid # the place where it would be 