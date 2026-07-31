class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # sort the array 
        nums.sort()

        # accumulator
        triples = []

        # for an arbitrary # in k 
        # Loop invariant: triples contains all triples in sorted_nums[..i]
        for k in range(len(nums)):
            if k == 0 or (k >= 1 and nums[k] != nums[k - 1]):
                target = nums[k] # this is the target
                i = k + 1
                j = len(nums) - 1
                while i < j:
                    if nums[i] + nums[j] > -1* target:
                        j -= 1
                    elif nums[i] + nums[j] < -1* target:
                        i += 1
                    else: 
                        triples.append([nums[k], nums[i], nums[j]])
                        i += 1
                        j -= 1

                        while nums[j] == nums[j + 1] and j > i:
                            j -= 1
                        
                        while nums[i] == nums[i - 1] and i < j:
                            i += 1
                # create triples
                # add triples to accumulator
        return triples
