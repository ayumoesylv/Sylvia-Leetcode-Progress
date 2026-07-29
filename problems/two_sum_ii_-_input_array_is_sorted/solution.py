class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) 

        while l < r:
            sum = numbers[l] + numbers[r - 1]
            if sum == target:
                return [l+1, r]
            elif sum > target:
                r -= 1
            else: 
                l += 1
        

