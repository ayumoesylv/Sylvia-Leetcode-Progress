class Solution {
    public int removeElement(int[] nums, int val) {
        int i = 0;
        int j = nums.length;
        while (i < j) {
            if (nums[i] == val) {
                swap(nums, i, j - 1);
                j--;
            } else {
                i++;
            }
        }
        return i;
    }

    private void swap(int[] nums, int first, int secnd) {
        int temp = nums[secnd];
        nums[secnd] = nums[first];
        nums[first] = temp;
    }
}