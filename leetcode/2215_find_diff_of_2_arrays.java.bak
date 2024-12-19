class Solution {
    public int pivotIndex(int[] nums) {
        int n = nums.length, i;
        int left_sum = 0, right_sum = 0;
        for(i=1;i<n;i++) right_sum += nums[i];
        if (left_sum==right_sum) return 0;
        for (i=1; i<n; i++)
        {
            left_sum += nums[i-1];
            right_sum -= nums[i];
            if (left_sum==right_sum) return i;
        }
        return -1;
    }
}