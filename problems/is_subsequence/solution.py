class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0 
        j = 0 
        while j < len(t) and i < len(s):
            # do modification
            # check t[j] char 
            if t[j] == s[i]: 
                # increment j
                # increment i 
                i += 1
                j += 1
            else: 
                # increment j 
                j += 1
        if i == len(s):
            return True 
        else: 
            return False