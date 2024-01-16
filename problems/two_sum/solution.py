class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                temp = nums[i] + nums[j] #this is the sum of the pairing
                if temp == target:
                    return [i, j]

solulu = Solution()
print(solulu)