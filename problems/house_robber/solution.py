class Solution:
    def _rob_helper(self, nums: List[int], first, memo: dict[int, int]):
        # Let the memo contain the max amount of money if you rob a house at index i
        if len(nums) == 0:
            return 0 
        elif len(nums) == 1:
            return nums[0]
        # if the nums is greater than 1
        rob_max = nums[0]
        no_rob_max = 0
        if first + 2 in memo: 
            rob_max += memo[first + 2]
        else: 
            val = self._rob_helper(nums[2:], first + 2, memo)
            memo[first + 2] = val 
            rob_max += val 
        
        if first + 1 in memo: 
            no_rob_max += memo[first + 1] 
        else:
            val = self._rob_helper(nums[1:], first + 1, memo)
            memo[first + 1] = val 
            no_rob_max += val
        return max(rob_max, no_rob_max)

    def rob(self, nums: List[int]) -> int:
        memo = {}
        return self._rob_helper(nums, 0, memo)