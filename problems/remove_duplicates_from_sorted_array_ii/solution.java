class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 1; // read pointer
        int j = 1; // write pointer 

        int numSeen = 1;
        
        while (i < nums.length) {
            // invariant: after reading the ith element, numSeen reflects how many between nums[k..i]
            
            if (nums[i] == nums[i - 1]) { // when they are same
                if (numSeen < 2) {
                    // update numSeen and write
                    numSeen++;
                    nums[j] = nums[i];
                    j++;
                } // else do nothing 
            } else { // when they are different -> means start new unique num
                // reset numSeen to 1
                numSeen = 1;
                nums[j] = nums[i];
                j++;
            }
            i++;
        }
        return j;
        
    }
}