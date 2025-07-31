class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x == 0:
            return True
        digits = 0
        while True: # this will yield the number of digits of x
            (q, r) = divmod(x, 10**digits)
            if r == x:
                break
            digits += 1
        
        power = digits - 1

        if digits == 1: 
            return True
        
        if digits == 2: 
            q, r = divmod(x, 10 ** power)
            return q == r
        
        q, r = divmod(x, 10 ** power)
        leftmost = q

        q, r = divmod(x, 10)
        rightmost = r

        middle = q - (leftmost * (10 ** (digits - 2)))

        # if the first element of divmod of the middle number and the second argument is 0, that means the number of digits of middle doesn't match with the expected number of digits for the recurse call, meaning there are leading zeros. This implies 
        lead_zero = divmod(middle, (10 ** (digits - 3)))[0]
        if lead_zero == 0:
            middle += (10 ** (digits - 3))
            middle += 1
        result = self.isPalindrome(middle)

        if leftmost == rightmost and result:
            return True
        return False
        # use recursion: base case ()
        
        # reverse = 0
        # for p in range(i): # if i is 3, as it would be for 121, p is 0, 1, 2
        #     q, r = divmod(x, 10 ** p)
        #     print(q, r)
        #     q /= (10 ** p)
        #     q *= (10 ** (2-p))
        #     reverse += q
        # print(reverse)
        # if x == reverse:
        #     return True
        # return False

