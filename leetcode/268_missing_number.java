class Solution {
    public int missingNumber(int[] nums) {
        int arrSum = 0;
        int arrMax = nums[0];
        for(int i=0; i<nums.length; i++){
            if (nums[i] > arrMax)
                arrMax = nums[i];
            arrSum += nums[i];
        }
        if (arrMax < nums.length)
            return nums.length;
        return (arrMax * (arrMax+1))/2 - arrSum;
    }
}
