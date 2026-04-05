class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] count = new int[101];
        
        // Count the frequency of each number
        for (int num : nums) {
            count[num]++;
        }
        
        // Compute running sum 
        for (int i = 1; i <= 100; i++) {
            count[i] += count[i - 1];
        }
        
        // Build the result array
        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                res[i] = 0;
            } else {
                res[i] = count[nums[i] - 1];
            }
        }
        
        return res;
    }
}
