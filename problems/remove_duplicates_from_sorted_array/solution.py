class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1 # Let k be the write pointer
        j = 1 # Let j be the read pointer

        # Loop invariant: `nums[..k]` is sorted and deduplicated. `nums[..j]` is sorted and deduplicated. `j` is greater or equal to `k`. 
        # End condition: When j = len(nums)
        while j < len(nums):
            # if nums[j] != nums[j - 1], then write that to k's position and increment k 
            if nums[j] != nums[j - 1]:
                nums[k] = nums[j]
                k += 1
            # increment j 
            j += 1
            # since nums is sorted, the only way a duplicate can exist is right beside its duplicates. Thus we don't need to check the whole array again
        return k