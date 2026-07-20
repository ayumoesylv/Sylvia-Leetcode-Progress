class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            sum = 0
            for x in nums:
                val = (x >> i) & 1
                sum += val 
            ans |= (sum % 3) << i 
        if ans >= (1 << 31):
            return ans - 2**32
        else:
            return ans
