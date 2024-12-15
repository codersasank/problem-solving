class Solution {
    public void moveZeroes(int[] nums) {
        int right=0, left = 0;
        int n = nums.length;
        while (left<n && right<n)
        {
            while (right<n && nums[right]==0)
                right++;
            if (right==n) return;
            if (left==right)
            {
                left++; right++;
                continue;
            }
            nums[left] = nums[right];
            nums[right] = 0;
            left++ ; right++;
        }
        
    }
}
