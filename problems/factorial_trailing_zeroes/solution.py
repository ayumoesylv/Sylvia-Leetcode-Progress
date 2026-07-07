class Solution:
    def trailingZeroes(self, n: int) -> int:
        current_power = 5
        total_fives = 0
        while current_power <= n:
            divisor = (n - (n % current_power)) // current_power 
            total_fives += divisor
            current_power *= 5
        return total_fives