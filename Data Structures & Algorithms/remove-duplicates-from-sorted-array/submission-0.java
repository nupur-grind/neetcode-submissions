class Solution {
    public int removeDuplicates(int[] nums) {
        //array nums, array numsuniq.length = k
        //loop if nums[i]==nums[i+1] then replace nums[i+1] with nums[i+2]
        //once done, give nums output and print k = nums.length

        int k = 1;
        for (int i = 1; i <= nums.length - 1; i++) {
            if (nums[i] != nums[i - 1]) {
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }
}