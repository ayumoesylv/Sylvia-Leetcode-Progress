class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # initialize a 32 bit number because of constraints 
        ans = 0
        for i in range(32):
            sum = 0
            for x in nums:
                # right shift to get to ith bit and check if 1 using bitmap
                val = (x >> i) & 1
                sum += val if val == 1 else 0
            sum %= 2 
            sum <<= i 
            ans |= sum 
        if ans >= 1 << 31:
            ans -= 1 << 32
        return ans
