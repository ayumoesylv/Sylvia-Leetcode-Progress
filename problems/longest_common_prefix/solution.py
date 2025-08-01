class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        find minimum length min_length = min([len(x) for x in strs])
        for i in range(min_length):
            if 
        issue is that this implementation requires nested loop
        """

        # brute force
        min_length = min([len(x) for x in strs])
        prefix = ''
        for i in range(min_length):
            letter = strs[0][i]
            for p in strs[1:]:
                if letter != p[i]:
                    return prefix
            prefix += letter
        return prefix




            
            