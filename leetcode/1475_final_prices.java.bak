class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int max_sum = 0, sum = 0, i, n = nums.length;
        float avg = 0;
        for(i=0; i<k; i++)
        {
            sum += nums[i];
        }
        max_sum = sum;
        for(i=k; i<n; i++)
        {
            sum -= nums[i-k];
            sum += nums[i];
            if (sum > max_sum) max_sum = sum;
        }
        return max_sum/(k*1.0);        
    }
}