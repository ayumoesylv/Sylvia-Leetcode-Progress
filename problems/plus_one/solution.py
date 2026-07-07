class Solution:
    def is_all_9(self, digits) -> bool:
        for digit in digits:
            if digit != 9:
                return False 
        return True

    def increase_all_9(self, digits):
        digits[0] = 1
        for i in range(1, len(digits)):
            digits[i] = 0
        digits.append(0)

    def plusOne(self, digits: List[int]) -> List[int]:
        # check if 9, 99, 999, 9999, 99999, ...
        if self.is_all_9(digits):
            self.increase_all_9(digits)
        else:
            ptr = len(digits) - 1
            while digits[ptr] == 9: 
                digits[ptr] = 0
                ptr -= 1
            digits[ptr] += 1
        return digits

            