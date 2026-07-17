class Solution:
    def _stairsHelper(self, hmap, n):
        if n == 1 or n == 0: # base case
            return 1
        elif n in hmap:
            return hmap[n]
        else: # add n - 1 and n - 2 together and return
            # check if n - 1 is in hmap
            if (n - 1) in hmap:
                one_step = hmap[n-1]
            else: # otherwise call climbstairs
                one_step = self._stairsHelper(hmap, n-1)
                hmap[n-1] = one_step
            
            if (n - 2) in hmap: # check if n - 2 is in hmap
                two_step = hmap[n-2]
            else: # otherwise call climbstairs
                two_step = self._stairsHelper(hmap, n-2)
                hmap[n-2] = two_step 
            return one_step + two_step
    def climbStairs(self, n: int) -> int:
        # check if n is in hmap, otherwise:
        hmap = {}
        stairs = self._stairsHelper(hmap, n)
        return stairs

        
            
        