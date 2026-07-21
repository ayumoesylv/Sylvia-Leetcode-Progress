class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # we can start from the back of the array and go down 
        # First identify where it starts. We are given non decreasing order
        pos1 = m - 1
        pos2 = n - 1
        i = m + n - 1

        while pos1 >= 0 and pos2 >= 0:
            if nums1[pos1] > nums2[pos2]: # take nums 1
                nums1[i] = nums1[pos1]
                i -= 1
                pos1 -= 1
            elif nums1[pos1] <= nums2[pos2]:
                nums1[i] = nums2[pos2]
                i -= 1
                pos2 -= 1
        if pos2 >= 0:
            for x in range(pos2, -1, -1):
                nums1[i] = nums2[pos2]
                i -= 1
                pos2 -= 1